Instruções para colocar o código a rodar:

Instalar as bibliotecas necessárias através de: pip install -r requirements.txt
Caso não exista o ficheiro ''requirements.txt'', instalar através de: pip install streamlit googlemaps tensorflow scikit-learn

Após instaladas as bibliotecas, o código requer uma API key do Google Maps, logo será necessário seguir os seguintes passos:
1º - Acessar ao Google Cloud Console
2º - Criar um novo projeto
3º - Ir a APIs & Serviços > Biblioteca
4º - Ativar as APIs: Directions API (Para as rotas); Distance Matrix API (Para o tempo de viagem) e Geocoding API (Converter os endereços)
Após isto, ir a APIs & Serviços > Credenciais, Criar Credenciais > API Key
Copiar esta API key e inserir no código no ficheiro ''otimizar_rotas.py''

Seguir a seguinte ordem ao correr o programa:
1º Rodar ''otimizar_rotas.py'', após ter inserido a sua API key no sítio indicado para tal;
2º Rodar ''interface.py'';
3º Rodar '' previsão_de_tráfego.py''.

Após seguir estes passos, o projeto correrá sem qualquer problema.