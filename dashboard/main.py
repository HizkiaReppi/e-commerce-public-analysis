from typing import Tuple, Union
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
import urllib.request
from functions import DataAnalyzer, BrazilMapPlotter
from babel.numbers import format_currency

# Set styles
sns.set(style='dark')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load dataset
datetime_cols = ["order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date", "order_purchase_timestamp", "shipping_limit_date"]
ecom_data = pd.read_csv("https://raw.githubusercontent.com/HizkiaReppi/e-commerce-public-analysis/main/datasets/e-commerce-df.csv")
ecom_data.sort_values(by="order_approved_at", inplace=True)
ecom_data.reset_index(inplace=True)

# Load geolocation dataset
geolocation = pd.read_csv('https://raw.githubusercontent.com/HizkiaReppi/e-commerce-public-analysis/main/datasets/customer_geolocation.csv')
geo_data = geolocation.drop_duplicates(subset='customer_unique_id')

st.title("E-Commerce Analysis Dashboard")

# Convert columns to datetime
for col in datetime_cols:
    ecom_data[col] = pd.to_datetime(ecom_data[col])

min_date = ecom_data["order_approved_at"].min()
max_date = ecom_data["order_approved_at"].max()

# Sidebar
with st.sidebar:
    st.title("Hizkia Jefren Reppi")
    start_date, end_date = st.date_input(
        label="Select Date Range",
        value=[min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Main
main_df = ecom_data[(ecom_data["order_approved_at"] >= str(start_date)) & 
                 (ecom_data["order_approved_at"] <= str(end_date))]

# Instantiate DataAnalyzer and BrazilMapPlotter
data_analyzer = DataAnalyzer(main_df)
map_plotter = BrazilMapPlotter(geo_data, plt, mpimg, urllib, st)

# Analyze data
daily_orders_df = data_analyzer.daily_orders_summary()
sum_spend_df = data_analyzer.total_spend_summary()
sum_order_items_df = data_analyzer.product_category_summary()
review_score, common_score = data_analyzer.review_score_summary()
state, most_common_state = data_analyzer.customer_state_summary()
order_status, common_status = data_analyzer.order_status_summary()

# Dashboard
st.header("E-Commerce Dashboard")

# Daily Orders
st.subheader("Daily Orders")
col1, col2 = st.columns(2)

with col1:
    total_order = daily_orders_df["order_count"].sum()
    st.markdown(f"Total Order: **{total_order}**")

with col2:
    total_revenue = format_currency(daily_orders_df["revenue"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Revenue: **{total_revenue}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    daily_orders_df["order_approved_at"],
    daily_orders_df["order_count"],
    marker="o",
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

# Customer Spend Money
st.subheader("Customer Spend Money")
col1, col2 = st.columns(2)

with col1:
    total_spend = format_currency(sum_spend_df["total_spend"].sum(), "IDR", locale="id_ID")
    st.markdown(f"Total Spend: **{total_spend}**")

with col2:
    avg_spend = format_currency(sum_spend_df["total_spend"].mean(), "IDR", locale="id_ID")
    st.markdown(f"Average Spend: **{avg_spend}**")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(
    sum_spend_df["order_approved_at"],
    sum_spend_df["total_spend"],
    marker="o",
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis="x", rotation=45)
ax.tick_params(axis="y", labelsize=15)
st.pyplot(fig)

# Order Items
st.subheader("Order Items")
col1, col2 = st.columns(2)

with col1:
    total_items = sum_order_items_df["product_count"].sum()
    st.markdown(f"Total Items: **{total_items}**")

with col2:
    avg_items = sum_order_items_df["product_count"].mean()
    st.markdown(f"Average Items: **{avg_items}**")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(45, 25))
colors = ["#068DA9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Top-selling Products", loc="center", fontsize=50)
ax[0].tick_params(axis ='y', labelsize=35)
ax[0].tick_params(axis ='x', labelsize=30)

sns.barplot(x="product_count", y="product_category_name_english", data=sum_order_items_df.sort_values(by="product_count", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Lowest-selling Products", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)

st.pyplot(fig)

with st.expander("See Explanation"):
    st.write("Based on the visualization results that have been displayed, it can be concluded that customers buy bed_bath_table products more often, and security_and_services products are the least frequently purchased.")

# Review Score
st.subheader("Review Score")
col1,col2 = st.columns(2)

with col1:
    avg_review_score = review_score.mean()
    st.markdown(f"Average Review Score: **{avg_review_score}**")

with col2:
    most_common_review_score = review_score.value_counts().index[0]
    st.markdown(f"Most Common Review Score: **{most_common_review_score}**")

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=review_score.index, 
            y=review_score.values, 
            order=review_score.index,
            palette=["#068DA9" if score == common_score else "#D3D3D3" for score in review_score.index]
            )

plt.title("Rating by customers for service", fontsize=15)
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(fontsize=12)
st.pyplot(fig)

with st.expander("See Explanation"):
    st.write("Customer satisfaction with the services provided is very satisfying because the visualization that has been displayed shows that there are very many customers who gave a rating of 5, and a rating of 4 is the 2nd most.")

# Customer Demographic
st.subheader("Customer Demographic")
tab1, tab2, tab3 = st.tabs(["State", "Order Status", "Geolocation"])

with tab1:
    most_common_state = state.customer_state.value_counts().index[0]
    st.markdown(f"Most Common State: **{most_common_state}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=state.customer_state.value_counts().index,
                y=state.customer_count.values, 
                data=state,
                palette=["#068DA9" if score == most_common_state else "#D3D3D3" for score in state.customer_state.value_counts().index]
                    )

    plt.title("Number customers from State", fontsize=15)
    plt.xlabel("State")
    plt.ylabel("Number of Customers")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

    with st.expander("See Explanation"):
        st.write("The user distribution by state indicates that the majority of customers are located in São Paulo (SP), constituting the largest user base with 41,746 customers. Other significant states include Rio de Janeiro (RJ) with 12,852 customers and Minas Gerais (MG) with 11,635 customers. The dataset also reflects user presence in states such as Rio Grande do Sul (RS), Paraná (PR), and Santa Catarina (SC), contributing to the platform's regional diversity.")

with tab2:
    common_status_ = order_status.value_counts().index[0]
    st.markdown(f"Most Common Order Status: **{common_status_}**")

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=order_status.index,
                y=order_status.values,
                order=order_status.index,
                palette=["#068DA9" if score == common_status else "#D3D3D3" for score in order_status.index]
                )
    
    plt.title("Order Status", fontsize=15)
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.xticks(fontsize=12)
    st.pyplot(fig)

    with st.expander("See Explanation"):
        st.write(
            "Delivered Orders:\n"
            "The majority of orders fall under the 'delivered' status, constituting a significant portion of the dataset (96,478). "
            "This indicates that a large number of customers have successfully received their orders.\n\n"
            
            "Shipped and Processing Orders:\n"
            "'Shipped' and 'processing' statuses represent ongoing order fulfillment. 'Shipped' has 1,107 orders, suggesting "
            "products are in transit to customers. 'Processing' includes 301 orders, indicating that they are in the pipeline for delivery.\n\n"
            
            "Cancelled and Unavailable Orders:\n"
            "A smaller portion of orders (625) is marked as 'canceled,' possibly due to customer requests or inventory issues. "
            "'Unavailable' status (609) may suggest products that are temporarily out of stock.\n\n"
            
            "Invoiced and Created Orders:\n"
            "'Invoiced' orders (314) typically imply that invoices have been issued but the products may not have been shipped yet. "
            "'Created' status (5) represents newly created orders that are in the early stages of processing.\n\n"
            
            "Approved Orders:\n"
            "Only 2 orders are marked as 'approved,' indicating that they have passed a certain approval stage."
        )

with tab3:
    map_plotter.plot_brazil_map()

    with st.expander("See Explanation"):
        st.write('According to the graph that has been created, there are more customers in the southeast and south. Other information, there are more customers in cities that are capitals (São Paulo, Rio de Janeiro, Porto Alegre, and others).')

st.caption('Copyright 2023 - Hizkia Jefren Reppi')

# Copyright 2023 - Hizkia Jefren Reppi
