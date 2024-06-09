
import pandas as pd
import streamlit as st
from resources.bucket_files import download_file_to_dataframe, aws_bucket, path_lambda, path_glue
from resources.process_tools import process_dataframe, display_results, create_expander_with_checkboxes
from resources.visual_tools import create_line_chart, create_success_card

st.set_page_config(layout="wide")

# Custom HTML/JS for the banner
custom_js = """
<script>
// Modify the decoration on top to reuse as a banner

// Locate elements
var decoration = window.parent.document.querySelectorAll('[data-testid="stDecoration"]')[0];
var sidebar = window.parent.document.querySelectorAll('[data-testid="stSidebar"]')[0];

// Observe sidebar size
function outputsize() {
    decoration.style.left = `${sidebar.offsetWidth}px`;
}

new ResizeObserver(outputsize).observe(sidebar);

// Adjust sizes
outputsize();
decoration.style.height = "3.0rem";
decoration.style.right = "45px";

// Adjust image decorations
decoration.style.backgroundImage = "url(resources/docker_monitoring.png)";
decoration.style.backgroundSize = "contain";
</script>        
"""

# Display the custom JS
st.components.v1.html(custom_js, width=0, height=0)


# Baixar os arquivos e armazenar no DataFrame
df_lambda = download_file_to_dataframe(aws_bucket, path_lambda)
df_glue = download_file_to_dataframe(aws_bucket, path_glue)


st.title("🔧 My Own loggin monitor tool")

# Adiciona conteúdo na barra lateral
st.sidebar.title('Last runs')
lambda_sidebar = process_dataframe(df_lambda)
display_results("Lambdas",lambda_sidebar)

glue_sidebar = process_dataframe(df_glue)
display_results("Glue",glue_sidebar)


st.sidebar.write('Contact - @gabrielphilot')

st.sidebar.markdown("[Repo-project](https://github.com/Gabriel-Philot/xpe_igti_pa)")
st.sidebar.markdown("[linkedin](https://www.linkedin.com/in/gabriel-philot/)")

st.subheader('📑 All information about Lambda and Glue runs [in AWS]')

with st.expander('Lambdas full runs'):
    st.write(df_lambda)

with st.expander('Glue full runs'):
    st.write(df_glue)

st.subheader('🎯 X - ray ingestion Lambdas')

x_ray_value = create_expander_with_checkboxes(df_lambda, 'name_fun')

with st.expander('Lambdas x-ray'):
    if x_ray_value:
        st.write(x_ray_value)
        create_success_card(df_lambda, x_ray_value)
        create_line_chart(df_lambda, x_ray_value)


st.subheader('🎯 X - ray process Glues')

x_ray_value_glue = create_expander_with_checkboxes(df_glue, 'name_fun')

with st.expander('Glues x-ray'):
    if x_ray_value_glue:
        st.write(x_ray_value_glue)
        create_success_card(df_glue, x_ray_value_glue)
        create_line_chart(df_glue, x_ray_value_glue)