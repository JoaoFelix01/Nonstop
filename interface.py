import streamlit as st
import requests
import matplotlib.pyplot as plt
import networkx as nx
import json

st.title("Nonstop: Melhor Rota em Lisboa")

#Entrada
origem = st.selectbox("Escolha o ponto de partida:", ["Rossio", "Alfama", "Belém", "Parque das Nações", "Bairro Alto"])
destino = st.selectbox("Escolha o destino:", ["Rossio", "Alfama", "Belém", "Parque das Nações", "Bairro Alto"])

if st.button("Calcular Rota"):
    response = requests.get(f"http://127.0.0.1:5000/get_route?origem={origem}&destino={destino}")
    if response.status_code == 200:
        data = response.json()
        st.success(f"Melhor rota: {' → '.join(data['rota'])}")
        st.info(f"Tempo estimado: {data['tempo_estimado']}")

        #Visualização do grafo
        G = nx.Graph()
        for i in range(len(data["rota"]) - 1):
            G.add_edge(data["rota"][i], data["rota"][i+1])

        pos = nx.spring_layout(G)
        plt.figure(figsize=(8,6))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray")
        st.pyplot(plt)
    else:
        st.error("Erro ao calcular a rota.")
