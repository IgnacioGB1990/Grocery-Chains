import streamlit as st
import json
import filter as fil
import pandas as pd
from streamlit_lottie import st_lottie
from PIL import Image
import numpy as np
import plotly.express as px
import pydeck as pdk
import time
import plotly.graph_objects as go

path = "./src/assets/shopping-options.json"
with open(path,"r") as file:
    url = json.load(file)

def home():    
       with st.container():        
        st.title('CompraSmart')
        st.write("----")
        st.write("##")
        st.subheader("Toma el control de tu cesta de la compra")
        st.write("##")
        st.write("Compara con otros supermercados de la zona para tomar la deción correcta sobre tu cesta de la compra ")
        st_lottie(url, reverse=True, height=500, width=500, speed=1, loop=True, quality='high',)
        st.write("----")




def carga_datos():
    uploaded_file = st.file_uploader("Cargar CSV", type=["csv"])
   
    if uploaded_file is not None:
        global dataset
        dataset = pd.read_csv(uploaded_file, parse_dates=["Date"])
        dataset["Date"] = dataset["Date"].dt.strftime('%d-%m-%Y')

        
        st.markdown("<h3 style='text-align: center; color: green;'>Mi lista de la compra</h3>", unsafe_allow_html=True)
        st.dataframe(dataset)
        pivot_table = pd.pivot_table(dataset, values="Price", columns="Shop", index="Date", aggfunc=np.sum).copy()
        st.markdown("<p style='text-align: center;'>Variación precio</p>", unsafe_allow_html=True)
    
        st.line_chart(pivot_table)    


def version_2():

    st.header("Trabajando en la versión 2.0  👨‍💻  ")

    with st.expander("Próximos supermercados:"):
        st.markdown("""
                * Carrefour \n
                * El Corte Inglés (Supermercado) \n
                * Dia \n
                * Lidl \n
                * Supercor \n
                * Eroski \n
                """)
    
    with st.expander("Nuevas funcionalidades de las que estamos muy emocionados:"):
        st.markdown("""
                * Geolocalización \n
                * Importar tu cesta \n
                * Análisis detallado de tu cesta \n
                * Y mucho más ... \n

                """)
    

def input_data():

    alimentos = st.text_input("Agrega alimentos")


