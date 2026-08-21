import streamlit as st
import pandas as pd
import numpy as np

# st.title("Mi primera aplicación en Streamlit")

# Texto y entradas
# nombre = st.text_input("Ingresa tu nombre:")
# if nombre:
#    st.write(f"¡Hola, {nombre}! Bienvenido a Streamlit.")

# Creación de un gráfico interactivo
# st.subheader("Datos de ejemplo")
# datos = pd.DataFrame(
#    np.random.randn(40, 3), columns=["Columna A", "Columna B", "Columna C"]
# )

# st.line_chart(datos)

# Título de la app
st.title("Visualizador de CSV")

# Cargar el archivo CSV (reemplaza 'datos.csv' por tu ruta o usa st.file_uploader)
# df = pd.read_csv("datos.csv")

st.subheader("Elige un archivo para visualizar")
archivo_subido = st.file_uploader("", type=["csv"])

if archivo_subido is not None:
    df = pd.read_csv(archivo_subido)
    st.dataframe(df)

    st.subheader("Cantidad de Consultas por Semana Epidemiológica")
    st.bar_chart(
        df["SEMEPI"].value_counts(),
        x_label="Semana Epidemiológica",
        y_label="Cantidad de Consultas",
    )
    st.bar_chart(df["DIAGNOSTIC"].value_counts())
    st.bar_chart(df["DIA"].value_counts())

    df_respiratorias = df[(df["DIAGNOSTIC"] == "RESPIRATORIASUP")]
    # st.dataframe(df_respiratorias)
    st.bar_chart(df_respiratorias["SEMEPI"].value_counts())
    # st.bar_chart(df[(df["DIAGNOSTIC"] == "RESPIRATORIASUP")])
# Mostrar como tabla interactiva
# st.dataframe(df)
