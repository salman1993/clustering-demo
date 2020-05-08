## Taken from https://docs.streamlit.io/tutorial/create_a_data_explorer_app.html

import streamlit as st
import pandas as pd
import plotly.express as px

st.title('CORD-19 Embedding - PCA Projections')

DATA_PATH = "cord19_projections.csv.gz"

@st.cache
def load_data(nrows=None):
    data = pd.read_csv(DATA_PATH, compression='gzip', nrows=nrows)
    data['cluster'] = data.cluster.astype('category')
    return data

data_load_state = st.text('Loading data...')
df = load_data(nrows=None)
data_load_state.text("Data loaded successfully!")

fig = px.scatter(df, x="z1", y="z2", color="cluster", 
            hover_data=df.columns, opacity=0.8, width=1000, height=800)
st.write(fig)
