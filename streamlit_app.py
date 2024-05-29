import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
@st.cache  # Esta línea hace que la carga de datos se almacene en caché
def load_data():
    data = pd.read_csv('IMDB-Movie-Data.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Visualizador de Datos del CSV')

# Mostrar las primeras filas del DataFrame
st.header('Primeras filas del dataset')
st.write(data.head())

# Seleccionar una columna para visualizar su histograma
st.header('Visualizar histograma de una columna')
column_to_plot = st.selectbox('Elige una columna para graficar', data.columns)
if st.button('Generar Histograma'):
    fig, ax = plt.subplots()
    data[column_to_plot].hist(ax=ax)
    ax.set_title(f'Histograma de {column_to_plot}')
    st.pyplot(fig)
