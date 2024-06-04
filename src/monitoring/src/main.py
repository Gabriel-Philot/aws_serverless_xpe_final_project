
import pandas as pd
import streamlit as st
from resources.bucket_files import download_file_to_dataframe, aws_bucket, path_lambda, path_glue


# Baixar os arquivos e armazenar no DataFrame
df_lambda = download_file_to_dataframe(aws_bucket, path_lambda)
df_glue = download_file_to_dataframe(aws_bucket, path_glue)




st.title("Monitoring Lambda and Glue execution in AWS")

st.write(df_lambda.head(20))
st.write(df_glue.head(20))