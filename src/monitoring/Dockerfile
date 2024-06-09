FROM python:3.12

# Atualizar pip e instalar dependências
RUN pip install --upgrade pip
RUN pip install streamlit pandas boto3 python-dotenv plotly

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY src/ /app

# Expor a porta usada pelo Streamlit
EXPOSE 8501

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "main.py"]