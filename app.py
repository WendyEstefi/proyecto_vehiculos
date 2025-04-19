import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    # Mensaje para el histograma
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico de histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    # Mensaje para el gráfico de dispersión
    st.write('Creación de un gráfico de dispersión para las columnas "odometer" y "price"')

    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre odómetro y precio")

    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
