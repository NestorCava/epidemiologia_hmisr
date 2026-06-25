import streamlit as st
import pandas as pd
import numpy as np

st.title("Mi primera aplicación en Streamlit")

# Texto y entradas
nombre = st.text_input("Ingresa tu nombre:")
if nombre:
    st.write(f"¡Hola, {nombre}! Bienvenido a Streamlit.")

# Creación de un gráfico interactivo
st.subheader("Datos de ejemplo")
datos = pd.DataFrame(
    np.random.randn(40, 3), columns=["Columna A", "Columna B", "Columna C"]
)

st.line_chart(datos)
