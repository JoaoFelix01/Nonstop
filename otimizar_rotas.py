import googlemaps
import networkx as nx
import time
import json
from flask import Flask, request, jsonify

#Configuração da API do Google Maps
API_KEY = "INTRODUZIR_API_CRIADA" #Consultar o ficheiro Readme.txt
gmaps = googlemaps.Client(key=API_KEY)

#Exemplos de locais em Lisboa
locations = {
    "Rossio": "Praça Dom Pedro IV, Lisboa",
    "Alfama": "Alfama, Lisboa",
    "Belém": "Belém, Lisboa",
    "Parque das Nações": "Parque das Nações, Lisboa",
    "Bairro Alto": "Bairro Alto, Lisboa"
}

#Gráfico de trânsito
G = nx.Graph()

#Função para obter o tempo de viagem
def get_travel_time(origin, destination, mode="driving"):
    try:
        directions = gmaps.directions(origin, destination, mode=mode, traffic_model="best_guess", departure_time="now")
        return directions[0]['legs'][0]['duration_in_traffic']['value'] / 60  #Tempo em minutos
    except:
        return float('inf')  #Caso falhe, devolve um tempo infinito

#Gráfico com tempos de viagem reais
for loc1 in locations:
    for loc2 in locations:
        if loc1 != loc2:
            travel_time = get_travel_time(locations[loc1], locations[loc2])
            G.add_edge(loc1, loc2, weight=travel_time)

#Criação de API Flask
app = Flask(__name__)

@app.route('/get_route', methods=['GET'])
def get_route():
    origem = request.args.get('origem')
    destino = request.args.get('destino')

    if origem not in G.nodes or destino not in G.nodes:
        return jsonify({"error": "Local não encontrado"})

    best_path = nx.shortest_path(G, source=origem, target=destino, weight="weight")
    best_time = nx.shortest_path_length(G, source=origem, target=destino, weight="weight")

    return jsonify({
        "rota": best_path,
        "tempo_estimado": f"{best_time:.2f} minutos"
    })

if __name__ == '__main__':
    app.run(debug=True)
