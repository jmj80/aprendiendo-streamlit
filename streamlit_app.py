import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
@st.cache  # Esta línea hace que la carga de datos se almacene en caché
def load_data():
    data = pd.read_csv('tu_ruta_al_archivo.csv')
    return data

data = load_data()

# Título de la aplicación
st.title('Visualizador de Datos del CSV')

# Utilizando st.columns para organizar las secciones
col1, col2 = st.columns(2)

with col1:
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

with col2:
    # Seleccionar una columna para visualizar el top 5 de películas
    st.header('Top 5 de películas según la columna seleccionada')
    column_to_sort_by = st.selectbox('Elige una columna para ver el top 5 de películas', data.columns, index=1)
    if st.button('Mostrar Top 5'):
        top_5_data = data.nlargest(5, column_to_sort_by)
        st.write(top_5_data[['Title', column_to_sort_by]])

    # Buscar y seleccionar una película para ver todos sus datos
    st.header('Buscar y ver datos de una película específica')
    movie_input = st.text_input('Escribe el título de una película')
    filtered_titles = data[data['Title'].str.contains(movie_input, case=False, na=False)]['Title'].tolist()
    movie_title = st.selectbox('Selecciona una película', filtered_titles)
    if st.button('Mostrar Datos de la Película Seleccionada'):
        movie_data = data[data['Title'] == movie_title]
        st.write(movie_data)


