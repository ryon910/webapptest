import streamlit as st
import pandas as pd

st.title("Streamlit")

df = pd.read_csv("webapptest/hotel.csv")
st.write(df)