

import pandas as pd # manejos de tablas
import numpy as np # calculos numericos
import matplotlib.pyplot as plt # constr. de graficos
import seaborn as sns # libreria de graficos
import scipy as sp # calculos complejos
import streamlit as st
import plotly.express as px





# _________________________________

st.title("Tabla Informativa")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

df = pd.read_csv("energy_sector_data_colombia.csv")
df
# Grafico de lineas
# Carga de datos (usando tus datos o datos de ejemplo)
try:
    df = pd.read_csv("energy_sector_data_colombia.csv")
    # Si deseas usar una columna específica como eje x, descomenta la siguiente línea y ajusta el nombre de la columna:
    # df = df.set_index('Nombre_de_la_columna_x') 
except FileNotFoundError:
    # Datos de ejemplo si no se encuentra el archivo
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.warning("Archivo 'energy_sector_data_colombia.csv' no encontrado. Se usan datos de ejemplo.")
    df = chart_data  # Asigna los datos de ejemplo a df

# Gráfico de líneas con Plotly
fig = px.line(df, 
              title='Gráfico de Líneas de Datos de Energía',
              labels={'value': 'Valor', 'index': 'Índice'})  # Ajusta las etiquetas si es necesario

# Personalización del gráfico (opcional)
fig.update_layout(xaxis_title='Eje X',  # Ajusta los títulos de los ejes
                  yaxis_title='Eje Y',
                  plot_bgcolor='white',  # Fondo blanco
                  font=dict(color='black'))  # Texto negro

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)




#_____________________________________________________________
# Cálculo de frecuencias
energy_counts = df['Energy_Type'].value_counts().reset_index()
energy_counts.columns = ['Energy_Type', 'Frecuencia']

# Creación del gráfico con Plotly
fig = px.bar(energy_counts, 
             x='Energy_Type', 
             y='Frecuencia',
             title='Cantidad de Typos de Energía',
             labels={'Frecuencia': 'Frecuencia'},
             color='Energy_Type')  # Colores para cada barra

# Personalización del gráfico (opcional)
fig.update_layout(xaxis_title='Energy_Type', 
                  yaxis_title='Frecuencia',
                  plot_bgcolor='white',  # Fondo blanco
                  font=dict(color='black'))  # Texto negro

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
#_____________________________________________

# Cálculo de frecuencias
energy_counts = df['Region'].value_counts().reset_index()
energy_counts.columns = ['Region', 'Frecuencia']

# Creación del gráfico con Plotly
fig = px.bar(energy_counts, 
             x='Region', 
             y='Frecuencia',
             title='Cantidad de Regiones',
             labels={'Frecuencia': 'Frecuencia'},
             color='Region')  # Colores para cada barra

# Personalización del gráfico (opcional)
fig.update_layout(xaxis_title='Region', 
                  yaxis_title='Frecuencia',
                  plot_bgcolor='white',  # Fondo blanco
                  font=dict(color='black'))  # Texto negro

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
