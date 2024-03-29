import streamlit as st
import pandas as pd
# import plotly.express as px
import numpy as np


import time
import functions as ft
import filter as fil
import plotlyGraphs as plG
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu


st.set_page_config(page_title="CompraSmart",page_icon=":tada",layout="wide")

df = pd.read_csv("src/dataCleaned/all_data.csv",parse_dates=["Fecha"])

change_text = """
<style>
span.st-ci.st-du.st-dt.st-f9.st-fa.st-af {max-width: 100%;}

</style>
"""
st.markdown(change_text, unsafe_allow_html=True)



# @st.cache_resource
# def load_data() -> pd.DataFrame:
#     return px.data.tips()

  
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["","Filtrar","Métricas","Mi compra","V 2.0"],
        icons=['house',"filter", 'graph-up', 'upload',"laptop"],
        menu_icon="cast",
        default_index=1,
    )

if selected == "":
    ft.home()
if selected =="Métricas":
    df_unique = df.drop_duplicates(subset = "Producto")
    st.plotly_chart(plG.build_bill_to_tip_figure(df))
    st.plotly_chart(plG.build_day_figure(df_unique))

    df_sin_mercadona = df.drop(df.loc[df['Supermercado']=="Mercadona"].index)
    df_sin_alcampo = df.drop(df.loc[df['Supermercado']=="Alcampo"].index)

    # st.plotly_chart(plG.build_bill_to_tip_figure(df_sin_mercadona))
    # st.plotly_chart(plG.build_bill_to_tip_figure(df_sin_alcampo))

    # st.plotly_chart(plG.time_series_graph(df_sin_mercadona))
    # st.plotly_chart(plG.test())

if selected =="Filtrar":
      st.dataframe(fil.filter_dataframe(df))
      ft.main()

if selected =="Mi compra":
    ft.carga_datos()

if selected =="V 2.0":
    ft.version_2()





    












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


      

# selected = option_menu(None, ["","Métricas","Filtrar","Cargar csv"], 
# icons=['house', 'graph-up', "filter", 'upload'], 
# menu_icon="cast", default_index=0, orientation="horizontal")
# selected




# testing 2

# with st.sidebar.selectbox("Elige una sección",("Region",  "Comparador","Variación de precios")):