from typing import Tuple, Union
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib.request
import streamlit as st
import pandas as pd

class DataAnalyzer:
    def __init__(self, ecom_data: pd.DataFrame):
        self.ecom_data = ecom_data

    def daily_orders_summary(self) -> pd.DataFrame:
        daily_orders_summary = self.ecom_data.resample(rule='D', on='order_approved_at').agg({
            "order_id": "nunique",
            "payment_value": "sum"
        }).reset_index()

        daily_orders_summary.rename(columns={
            "order_id": "order_count",
            "payment_value": "revenue"
        }, inplace=True)

        return daily_orders_summary

    def total_spend_summary(self) -> pd.DataFrame:
        total_spend_summary = self.ecom_data.resample(rule='D', on='order_approved_at').agg({
            "payment_value": "sum"
        }).reset_index()

        total_spend_summary.rename(columns={
            "payment_value": "total_spend"
        }, inplace=True)

        return total_spend_summary

    def product_category_summary(self) -> pd.DataFrame:
        product_category_summary = self.ecom_data.groupby("product_category_name_english")["product_id"].count().reset_index()
        product_category_summary.rename(columns={
            "product_id": "product_count"
        }, inplace=True)
        product_category_summary = product_category_summary.sort_values(by='product_count', ascending=False)

        return product_category_summary

    def review_score_summary(self) -> Tuple[pd.Series, Union[int, float]]:
        review_scores = self.ecom_data['review_score'].value_counts().sort_values(ascending=False)
        most_common_score = review_scores.idxmax()

        return review_scores, most_common_score

    def customer_state_summary(self) -> Tuple[pd.DataFrame, Union[int, float]]:
        customer_state_summary = self.ecom_data.groupby(by="customer_state").customer_id.nunique().reset_index()
        customer_state_summary.rename(columns={
            "customer_id": "customer_count"
        }, inplace=True)
        most_common_state = customer_state_summary.loc[customer_state_summary['customer_count'].idxmax(), 'customer_state']
        customer_state_summary = customer_state_summary.sort_values(by='customer_count', ascending=False)

        return customer_state_summary, most_common_state

    def order_status_summary(self) -> Tuple[pd.Series, Union[int, float]]:
        order_status_summary = self.ecom_data["order_status"].value_counts().sort_values(ascending=False)
        most_common_status = order_status_summary.idxmax()

        return order_status_summary, most_common_status


class BrazilMapPlotter:
    def __init__(self, geo_data: pd.DataFrame, plt: plt, mpimg: mpimg, urllib: urllib, st: st):
        self.geo_data = geo_data
        self.plt = plt
        self.mpimg = mpimg
        self.urllib = urllib
        self.st = st

    def plot_brazil_map(self):
        brazil_map = self.mpimg.imread(self.urllib.request.urlopen(
            'https://i.pinimg.com/originals/3a/0c/e1/3a0ce18b3c842748c255bc0aa445ad41.jpg'), 'jpg')
        ax = self.geo_data.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat",
                                figsize=(10, 10), alpha=0.3, s=0.3, c='maroon')
        self.plt.axis('off')
        self.plt.imshow(brazil_map, extent=[-73.98283055, -33.8, -33.75116944, 5.4])
        self.st.pyplot()
