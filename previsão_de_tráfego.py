import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import random

#Simulação de dados
np.random.seed(42)
horas = np.linspace(0, 23, 1000)
congestionamento = np.sin(horas/3) + np.random.normal(0, 0.2, len(horas))  #Simulação do trânsito

#Estrutura de dados para LSTM
df = pd.DataFrame({"hora": horas, "congestionamento": congestionamento})
scaler = MinMaxScaler()
df["congestionamento"] = scaler.fit_transform(df[["congestionamento"]])

X, y = [], []
for i in range(10, len(df)-1):
    X.append(df["congestionamento"].values[i-10:i])
    y.append(df["congestionamento"].values[i+1])

X, y = np.array(X), np.array(y)
X = np.expand_dims(X, axis=-1)

#Modelo LSTM
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(10, 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10, batch_size=16)

#Função para prever o congestionamento futuro
def predict_traffic(hora):
    hora = np.array([[hora / 23]])  #Normaliza à hora
    return scaler.inverse_transform(model.predict(hora.reshape(1, 1, 1)))[0][0]

#Teste de previsão
print(f"Previsão de tráfego às 18h: {predict_traffic(18)}")
