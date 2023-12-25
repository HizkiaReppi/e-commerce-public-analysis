# E-Commerce Public Data Analysis with Python - Dicoding

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Overview Project](#overview-project)

## Overview
Welcome to the E-Commerce Public Data Analysis project! This project is dedicated to analyzing and visualizing data from the E-Commerce Public Dataset. Whether you are interested in exploring the intricacies of e-commerce patterns or seeking insights into customer behavior, this project has got you covered.

## Project Structure
- `dashboard/`: This directory contains `dashboard.py`, which is used to create dashboards of data analysis results.
- `datasets/`: Directory containing the raw CSV data files.
- `E-Commerce-Analysis.ipynb`: This Jupyter Notebook file is used to perform data analysis.
- `README.md`: This documentation file.
- `requirements.txt`: This file lists all required Python libraries.

## Installation
1. Clone this repository to your local machine:
   ```
   git clone https://github.com/HizkiaReppi/e-commerce-public-analysis.git
   ```
2. Go to the project directory
   ```
   cd e-commerce-public-analysis
   ```
3. Install the required Python packages by running:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. **Data Wrangling**: Explore and run data wrangling scripts available in the `E_Commerce_Analysis.ipynb` file to prepare and clean the data.

2. **Exploratory Data Analysis (EDA)**: Use the provided Python scripts to explore and analyze the data. EDA insights can guide your understanding of e-commerce public data patterns.

3. **Visualization**: Experience interactive data exploration by running the Streamlit dashboard:
   ```
   cd dashboard
   streamlit run main.py
   ```
   Access the dashboard in your web browser at `http://localhost:8501`.

## Data Sources
The project uses the E-Commerce Public Dataset from [Belajar Analisis Data dengan Python's Final Project](https://drive.google.com/file/d/1MsAjPM7oKtVfJL_wRp1qmCajtSG1mdcK/view) offered by [Dicoding](https://www.dicoding.com/).

Feel free to explore the [E-Commerce Data Dashboard](https://e-commerce-public-analysis-hizkia.streamlit.app/) and delve into the fascinating world of e-commerce analytics!

## Overview Project

The E-Commerce Public Data Analysis project has successfully delved into the intricacies of the provided dataset, offering valuable insights and visualizations. Here are the key conclusions and findings derived from this project:

### 1. **Order Status Overview:**
   - **Delivered Orders (96,478):** The majority of orders are marked as "delivered," indicating successful order fulfillment.
   - **Shipped and Processing Orders (1,107 and 301):** "Shipped" suggests products are in transit, while "processing" indicates orders in the pipeline.
   - **Cancelled and Unavailable Orders (625 and 609):** A smaller portion of orders is marked as "canceled" or "unavailable," possibly due to customer requests or inventory issues.
   - **Invoiced and Created Orders (314 and 5):** "Invoiced" orders imply issued invoices, while "created" status represents newly created orders in early processing stages.
   - **Approved Orders (2):** Only two orders are marked as "approved," indicating they have passed a certain approval stage.

### 2. **Geographical Customer Distribution:**
   - The graphical representation of customer geolocation reveals a concentration of customers in the southeast and south regions, with prominent presence in capital cities such as São Paulo, Rio de Janeiro, and Porto Alegre.

### 3. **Daily Orders and Revenue:**
   - The daily orders graph provides a trend analysis, showcasing the fluctuation in order count over time.
   - Key metrics include the total number of orders and total revenue, offering a comprehensive view of the e-commerce performance during the selected date range.

### 4. **Customer Spending Behavior:**
   - A detailed exploration of customer spending behavior includes the total spend and average spend metrics, shedding light on overall customer financial engagement with the platform.

### 5. **Product Category Analysis:**
   - Top-selling and lowest-selling product categories are visualized, offering a quick overview of popular and less popular items.

### 6. **Review Scores:**
   - Average review score and the most common review score are highlighted, providing insights into customer satisfaction and sentiment.

### 7. **Customer Demographics:**
   - Customer distribution by state is presented, showcasing the most common state with the highest number of customers.

### 8. **Order Status Summary:**
   - A detailed explanation of different order statuses, including their meanings and counts, provides a comprehensive understanding of the order processing pipeline.

The interactive [E-Commerce Data Dashboard](https://e-commerce-public-analysis-hizkia.streamlit.app/) enhances the user experience, allowing for dynamic exploration of these conclusions. Whether you are a data enthusiast, business analyst, or decision-maker, this project equips you with valuable information to make informed decisions in the e-commerce domain.

Copyright 2023 - Hizkia Jefren Reppi
