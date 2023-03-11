import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="CompraSmart",page_icon=":tada",layout="wide")

path = "./src/assets/shopping-options.json"
with open(path,"r") as file:
    url = json.load(file)


# selected2 = option_menu(None, ["Home","Region","Comparador"], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2


# testing

# with st.sidebar.selectbox("Elige una sección",("Region",  "Comparador","Variación de precios")):

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["Home","Region","Comparador"],
        icons=['house', 'book',"envelope"],
        menu_icon="cast",
        default_index=0,
    )
if selected =="Home":
    with st.container():
        # st.write("----")
        left_column, right_column =st.columns(2)
        with left_column:
            st.title('CompraSmart')
            st.write("##")
            st.subheader("Encuentra el mejor super para hacer la compra de la semana")
            st.write("##")
            st.write("Agrega tus productos a la cesta y analiza en qué supermercado te conviene más hacer la compra")
        with right_column:
            st_lottie(url,
        reverse=True,
        height=500,
        width=500,
        speed=1,
        loop=True,
        quality='high',
    
    ) 
if selected =="Region":
    st.title(f"You have selected {selected}")
if selected =="Comparador":
    st.title(f"You have selected {selected}")











# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", 'Settings'], 
#         icons=['house', 'gear'], menu_icon="cast", default_index=1)
#     selected

# # 2. horizontal menu

# # 3. CSS style definitions
# selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )


      

  
     