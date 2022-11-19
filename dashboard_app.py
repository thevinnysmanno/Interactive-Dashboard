import pandas as pd
import streamlit as st
import plotly as px

st.set_page_config(
      page_title="Sales Dashboard",
      page_icon=':bar_chart:',
      layout='wide'
)

df = pd.read_excel(
      io= 'supermarkt_sales.xlsx',
      engine= 'openpyxl',
      sheet_name= 'Sales',
      skiprows= 3,
      usecols= 'B:R',
      nrows= 1000
)

# Filter
st.sidebar.header("Filter")

city = st.sidebar.multiselect(
      "Select City",
      options = df["City"].unique(),
      default= df["City"].unique()
)

customer_type = st.sidebar.multiselect(
      "Select Customer Type",
      options = df["Customer_type"].unique(),
      default= df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
      "Select Gender",
      options = df["Gender"].unique(),
      default= df["Gender"].unique()
)

df_selection = df.query(
      "City == @city & Customer_type == @customer_type & Gender == @gender"
)
