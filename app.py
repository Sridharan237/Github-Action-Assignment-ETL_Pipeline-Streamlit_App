import streamlit as st
import pandas as pd
import datetime

# Function to load data
def load_data():
    data = pd.read_csv('sales_data.csv')
    return data

# Function to transform data
def transform_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Sales_to_Profit_Ratio'] = df['Sales'] / df['Profit']
    df['Cumulative_Sales'] = df['Sales'].cumsum()
    return df

# Function to extract summary statistics
def get_summary_statistics(df):
    summary = df.describe()
    return summary

# Define the log file
log_file = 'runtime_log.txt'

def log_message(message):
    with open(log_file, 'a') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')

# Main function to run the Streamlit app
def main():
    st.title("ETL Process for Sales Data")
    
    # Step 1: Extract
    st.header("Step 1: Extract")
    data = load_data()
    print(data)
    print(type(data))   # data - type(<class 'pandas.core.frame.DataFrame'>)
    st.subheader("Raw Data")
    st.table(data)
    df_summary_statistics = get_summary_statistics(data)
    print(df_summary_statistics)
    
    # Step 2: Transform
    st.header("Step 2: Transform")
    transformed_data = transform_data(data)
    print(transformed_data)
    print(type(transformed_data))   # transformed_data - type(<class 'pandas.core.frame.DataFrame)
    st.subheader('Transformed Data')
    st.table(transformed_data)
    transformed_df_summary_statistics = get_summary_statistics(transformed_data)
    print(transformed_df_summary_statistics)
    
    # Load data
    st.header("Step 3: Load data")
    transformed_data.to_csv('tranformed_data.csv', index=False)
    
    # Generate Run time log
    log_message(f'ETL job completed and data saved to transformed_data.csv')
    
    # showing the contents in the file in streamlit app
    with open(log_file, 'r') as f:
        contents = f.read()
    
    st.header('Runtime Logs')
    st.write(contents)
    
main()