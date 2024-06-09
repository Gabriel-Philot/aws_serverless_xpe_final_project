import streamlit as st
import pandas as pd


def process_dataframe(df):
    df_sorted = df.sort_values(by='timestamp', ascending=False)
    df_filtered = df_sorted.groupby('name_fun').head(1)

    result_df = df_filtered[['timestamp', 'name_fun', 'success']]
    
    return result_df


def display_results(text, df):
    st.sidebar.write(f'{text}')
    

    def highlight_success(val):
        color = 'green' if val == 'sucess' else 'red'
        return f'background-color: {color}'
    
    styled_df = df.style.applymap(highlight_success, subset=['success'])
    st.sidebar.dataframe(styled_df)


# def create_selectbox(df, column_name):
#     unique_values = df[column_name].unique()
#     selected_value = st.selectbox(f'Selecione um valor de {column_name}', unique_values)
#     return selected_value


def create_expander_with_checkboxes(df, column_name):
    unique_values = df[column_name].unique()
    selected_values = []
    
    with st.expander(f'Chose the source {column_name}'):
        for value in unique_values:
            if st.checkbox(value):
                selected_values.append(value)
    
    return selected_values[0] if selected_values else None