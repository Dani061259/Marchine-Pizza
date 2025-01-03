



# Prevendo o preço de uma pizza através do input de diâmetro, através da ferramenta Marchine in learning
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
df = df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df [["diametro"]]
y = df [["preco"]]
modelo.fit(x, y)
st.title("prevendo o valor de uma pizza")
st.divider()
diametro = st.number_input("Digite o tamanho do diâmetro da pizza: ")
if diametro:    
      preco_previsto = modelo.predict([[diametro]])[0][0]
st.write(f"o valor da pizza com diâmetro de {diametro:.2f} é de R${preco_previsto:.2f}.")
