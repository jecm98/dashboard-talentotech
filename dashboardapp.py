

import pandas as pd # manejos de tablas
import numpy as np # calculos numericos
import matplotlib.pyplot as plt # constr. de graficos
import seaborn as sns # libreria de graficos
import scipy as sp # calculos complejos
import streamlit as st
import plotly.express as px




st.title("Tabla Informativa")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

df = pd.read_csv("energy_sector_data_colombia.csv")
df

# Cálculo de frecuencias
energy_counts = df['Energy_Type'].value_counts().reset_index()
energy_counts.columns = ['Energy_Type', 'Frecuencia']

# Creación del gráfico con Plotly
fig = px.bar(energy_counts, 
             x='Energy_Type', 
             y='Frecuencia',
             title='Frecuencia de Energy_Type',
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
             title='Frecuencia de Region',
             labels={'Frecuencia': 'Frecuencia'},
             color='Region')  # Colores para cada barra

# Personalización del gráfico (opcional)
fig.update_layout(xaxis_title='Region', 
                  yaxis_title='Frecuencia',
                  plot_bgcolor='white',  # Fondo blanco
                  font=dict(color='black'))  # Texto negro

# Mostrar el gráfico en Streamlit
st.plotly_chart(fig)
