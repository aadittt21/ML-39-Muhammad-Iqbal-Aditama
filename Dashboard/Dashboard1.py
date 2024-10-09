import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
colors = sns.color_palette("husl", 4)
sns.set(style="dark")

def create_byseaon_df(df, isseasonbyint):
    byseason_df = day_df.groupby(by="season")['instant'].nunique().reset_index()
    byseason_df.rename(columns={
        "instant": "customer_count"
    }, inplace=True)

    plt.figure(figsize=(10, 5))

    sns.barplot(
        y="customer_count",
        x="season",
        data=byseason_df.sort_values(by="customer_count", ascending=False),
        palette=colors
    )
    plt.title("Number of Customer by season", loc="center", fontsize=15)
    plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
    plt.ylabel('jumlah')
    plt.xlabel('musim')
    plt.tick_params(axis='x', labelsize=12)
    plt.show()
    
    return byseason_df

# Load datasets
day_df = pd.read_csv("D:\Python\day.csv")

# Sort values and convert date column
column = "dteday"
day_df.sort_values(by=column, inplace=True)
day_df.reset_index(drop=True, inplace=True)

day_df[column] = pd.to_datetime(day_df[column])

# Get date range
min_date = day_df[column].min()
max_date = day_df[column].max()

with st.sidebar:
    st.image("D:\Kuliah\Bangkit\Proyek Dicoding\model_Synapse_Carbon_C23.jpg")

    # Date input for selecting time range
    start_date, end_date = st.date_input(label="Time", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    
# Convert start_date and end_date to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataframes by selected date range
main_df = day_df[(day_df[column] >= start_date) & (day_df[column] <= end_date)]

# Create dataframes for visualizations
byseason_df = create_byseaon_df(main_df, 0)

# Dashboard content
st.header("Bikes")

col1 = st.columns(1)

# Barplot for time of day analysis
st.subheader("Number of Customer by Season")

fig3 = plt.figure(figsize=(10, 5))
sns.barplot(
    y="customer_count", 
    x="season", 
    data=byseason_df.sort_values(by="customer_count", ascending=False), 
    palette=colors
)
plt.title("Number of Customer by Season", loc="center", fontsize=17)
plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis="x", labelsize=12)
st.pyplot(fig3)