import streamlit as st
import pandas as pd
import plotly.express as px


def create_line_chart(df, selected_function):
    # Filtrar o DataFrame pela função selecionada
    df_filtered = df[df['name_fun'] == selected_function].copy()
    
    # Converter timestamp para datetime se necessário
    if not pd.api.types.is_datetime64_any_dtype(df_filtered['timestamp']):
        df_filtered['timestamp'] = pd.to_datetime(df_filtered['timestamp'])
    
    # Converter timestamp para yyyy-mm-dd
    df_filtered['timestamp'] = df_filtered['timestamp'].dt.strftime('%Y-%m-%d')
    
    # Gráfico de linha: tempo de execução ao longo do tempo
    line_chart = px.line(df_filtered, x='timestamp', y='time', title=f'Execution time (s)')
    
    # Exibir o gráfico no Streamlit
    st.plotly_chart(line_chart)


def create_success_card(df, selected_function):
    # Filter the DataFrame by the selected function
    df_filtered = df[df['name_fun'] == selected_function]
    
    # Calculate the success percentage and total number of runs
    total_runs = len(df_filtered)
    success_runs = len(df_filtered[df_filtered['success'] == 'sucess'])
    success_percentage = (success_runs / total_runs) * 100
    
    # HTML and CSS for the card with a transparent background
    card_html = f"""
    <div style="background-color:rgba(0, 0, 0, 0); color:#FFFFFF; padding: 20px; border-radius: 10px; border: 2px solid #FFFFFF; text-align: center; width: 300px; margin: auto;">
        <h3 style="margin: 0;">Success Percentage for {selected_function}</h3>
        <h1 style="margin: 10px 0;">{success_percentage:.2f}%</h1>
        <p style="margin: 0;">Total runs: {total_runs}</p>
    </div>
    """
    
    # Display the card in Streamlit
    st.markdown(card_html, unsafe_allow_html=True)