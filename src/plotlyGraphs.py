

import pandas as pd

import plotly.graph_objs as go
import plotly.express as px
import streamlit as st

def build_bill_to_tip_figure(df: pd.DataFrame) -> go.Figure:
    fig = px.scatter(
        df,
        "Categoría",
        "Precio (€)",
        color="Precio (€)",
        color_discrete_sequence=["rgba(99, 110, 250, 0.2)", "rgba(99, 110, 250, 1)"],
        category_orders={"selected": [False, True]},
        hover_data=[
            "Producto",
            "Precio (€)",
            "Supermercado"
        ],
        height=900,
    )
    fig.update_layout(paper_bgcolor="#FFFFFF", plot_bgcolor="#FFFFFF")
    fig.update_xaxes(gridwidth=0.1, gridcolor="#EDEDED")
    fig.update_yaxes(gridwidth=0.1, gridcolor="#EDEDED")
    return fig

def build_day_figure(df: pd.DataFrame) -> go.Figure:
    return px.histogram(
        df,
        "Categoría",
        color="Supermercado",
        color_discrete_sequence=["rgba(99, 110, 250, 1)", "rgba(99, 110, 250, 0.2)"],
        # category_orders={
        #     "selected": [True, False],
        #     "Fecha": ["Thur", "Fri", "Sat", "Sun"],
        # },
        height=600,
    )

def time_series_graph(df: pd.DataFrame) -> go.Figure:
    fig = go.Figure([go.Scatter(x=df['Fecha'], y=df['Precio (€)'])])
    return fig



# def time_series_graph(df: pd.DataFrame) -> go.Figure:
#     fig = px.line(df,x=df["Fecha"],y="Precio (€)",color="Producto")
#     fig.update_layour(hovermode="x")

def test():
    stocks = pd.read_csv("https://www.sharpsightlabs.com/datasets/amzn_goog_2000-01-01_to_2020-12-05.csv")
    stocks.date = pd.to_datetime(stocks.date)
    amazon_stock = stocks.query("stock == 'amzn'")
    px.line(data_frame = amazon_stock, x = 'date', y = 'close')