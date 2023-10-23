import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit")

df = pd.read_csv("/Users/owner/Desktop/Tech0/STEP2/Web_Application/20231009 ver1/02_前提知識/2a楽天api/hotel.csv")
st.write(df)