import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
colors = sns.color_palette("husl", 4)
sns.set(style="dark")

def create_byseason_df(df, isseasonbyint):
    byseason_df = df.groupby(by="season")['instant'].nunique().reset_index()
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

def create_byweekday_df(df, isweekdaybyint):
    byweekday_df = df.groupby(by="weekday")['instant'].nunique().reset_index()
    byweekday_df.rename(columns={
        "instant": "customer_count"
    }, inplace=True)

    plt.figure(figsize=(10, 5))

    sns.barplot(
    y="customer_count",
    x="weekday",
    data=byweekday_df.sort_values(by="customer_count", ascending=False),
    palette=colors
    )
    plt.title("Number of Customer by weekday", loc="center", fontsize=15)
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
    plt.ylabel('jumlah')
    plt.xlabel('day')
    plt.tick_params(axis='x', labelsize=12)
    plt.show()
    
    return byweekday_df

# Load datasets
day_df = pd.read_csv("https://raw.githubusercontent.com/aadittt21/ML-39-Muhammad-Iqbal-Aditama/faa68245eb101f126795f244f4453012d88469b0/Dashboard/day.csv")

# Sort values and convert date column
column = "dteday"
day_df.sort_values(by=column, inplace=True)
day_df.reset_index(drop=True, inplace=True)

day_df[column] = pd.to_datetime(day_df[column])

# Get date range
min_date = day_df[column].min()
max_date = day_df[column].max()

with st.sidebar:
    st.image("https://github.com/aadittt21/ML-39-Muhammad-Iqbal-Aditama/blob/faa68245eb101f126795f244f4453012d88469b0/Dashboard/model_Synapse_Carbon_C23.jpg?raw=true")

    # Date input for selecting time range
    start_date, end_date = st.date_input(label="Time", min_value=min_date, max_value=max_date, value=[min_date, max_date])
    
# Convert start_date and end_date to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataframes by selected date range
main_df = day_df[(day_df[column] >= start_date) & (day_df[column] <= end_date)]

# Create dataframes for visualizations
byseason_df = create_byseason_df(main_df, 0)
byweekday_df = create_byweekday_df(main_df, 0)

# Dashboard content
st.header("Bikes")

col1, col2 = st.columns(2)

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

st.subheader("Number of Customer by Weekday")
fig1 = plt.figure(figsize=(10,5))
sns.barplot(
    y="customer_count",
    x="weekday",
    data=byweekday_df.sort_values(by="customer_count", ascending=False),
    palette=colors
)
plt.title("Number of Customer by weekday", loc="center", fontsize=15)
plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
plt.ylabel('jumlah')
plt.xlabel('day')
plt.tick_params(axis='x', labelsize=12)
st.pyplot(fig1)
