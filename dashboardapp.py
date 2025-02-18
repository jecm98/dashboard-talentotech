

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

