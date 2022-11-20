import pandas as pd
import streamlit as st
import plotly.express as px

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

# Main Page
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(),1)
star_rating = ":star:" * int(round(average_rating,0))
average_transaction = round(df_selection["Total"].mean(), 2)

left_col, mid_col, right_col = st.columns(3)

with left_col:
      st.subheader("Total Sales")
      st.subheader(f"US $ {total_sales:,}")

with mid_col:
      st.subheader("Rating")
      st.subheader(f"{average_rating} {star_rating}")

with right_col:
      st.subheader("Average Transaction")
      st.subheader(f"US $ {average_transaction}")

st.markdown("---")

sales_by_product_line = (
      df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

fig_product_sales = px.bar(
      sales_by_product_line,
      x= "Total",
      y= sales_by_product_line.index,
      orientation= 'h',
      title= "<b>Sales By Product Line</b>",
      color_discrete_sequence= ["#0083B8"] * len(sales_by_product_line),
      template= "plotly_white",

)

fig_product_sales.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
})

st.plotly_chart(fig_product_sales)