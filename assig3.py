import pandas as pd
df = pd.read_csv('C:\\Users\\Katia\\Downloads\\mieszkania_windows.csv')
dfy = df.groupby(df['Rok'])['Wartosc'].mean()
import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm
StreamlitPatcher().jupyter()
st.dataframe(dfy.to_frame())