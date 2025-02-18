

import pandas as pd # manejos de tablas
import numpy as np # calculos numericos
import matplotlib.pyplot as plt # constr. de graficos
import seaborn as sns # libreria de graficos
import scipy as sp # calculos complejos
import streamlit as st




st.title("Tabla Informativa")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

df = pd.read_csv("energy_sector_data_colombia.csv")
df

print(df.describe())

print(df['Energy_Type'].value_counts())

# Grafico Barras

import streamlit as st
from vega_datasets import data
numerical_cols = [
    "Production_MWh", "Consumption_MWh", "Renewable_Percentage",
    "CO2_Emissions", "Investment_MillionUSD", "Energy_Cost_USD_per_kWh", "Energy_Loss_Percentage"
]
df_numeric = df.select_dtypes(include=['number'])
df_numeric = df[numerical_cols]
source = df_numeric()

st.bar_chart(source, x="Production_MWh", y="Consumption_MWh", color="site", stack=False)
