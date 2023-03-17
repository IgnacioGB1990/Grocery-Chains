from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
import pandas as pd

import plotly.graph_objs as go
import plotly.express as px
import streamlit as st

import plotlyGraphs as plG




# https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    

    modify = st.checkbox("Deshacer")

    if modify:
        return df

    df = df.copy()

    # Try to convert datetimes into a standard format (datetime, no timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])  
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Por columna", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            
            # # Treat columns with < 30 unique values as categorical
            if is_categorical_dtype(df[column]) or df[column].nunique() < 30:
                user_cat_input = right.multiselect(
                    f"{column}", df[column].unique(), default=list(df[column].unique()),                
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Rango de {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"{column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:

                df_unique = df.drop_duplicates(subset = "Producto")
                selected_products = st.multiselect("Producto", df_unique["Producto"])
                
 
                

                if selected_products:
                    st.markdown("<h3 style='text-align: blue; color: green;'>Evolución de Precios:</h3>", unsafe_allow_html=True)
                    st.write(selected_products[0])

                    product_chosen = selected_products[0]
                    new_df = pd.read_csv("src/dataCleaned/all_data.csv",parse_dates=["Fecha"])
                    time_series = new_df[new_df["Producto"]==f"{product_chosen}"]
                    st.plotly_chart(plG.time_series_graph(time_series))
                    
                    # fig = go.Figure([go.Scatter(x=time_series['Fecha'], y=time_series['Precio (€)'])])
                    # return fig


                # user_text_input = right.text_input(f"Filtra por {column}",  )

                # if user_text_input:
                #     pass

                #     # df = df[df[column].astype(str).str.contains(user_text_input)]
                #     # df = df[        df["Producto"].astype(str).str.contains(user_text_input)      ]

                    # df['Producto'] = df['Producto'].str.lower()
                    # df = df[        df["Producto"].str.contains(user_text_input.lower())      ]

                   

                 
    return df



