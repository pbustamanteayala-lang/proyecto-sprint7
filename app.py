import streamlit as st
import pandas as pd
import plotly as py

car_data = pd.read_csv('vehicles_us.csv')
df = pd.DataFrame(car_data)

st.header('Vehicles data')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir histograma')
 
# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
 
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
 
    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')
 
    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Ahora vamos a hacer un boton para grafico de dispersion 
disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión utilizando plotly.graph_objects
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)