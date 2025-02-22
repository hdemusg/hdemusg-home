import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Sumedh Surya Garimella", page_icon=":computer:")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Abel&family=Barlow:wght@300&family=Didact+Gothic&display=swap');

			* {
			font-family: 'Abel', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

st.title('Sumedh Surya Garimella')

st.subheader('Welcome to my portfolio page!')

text = pd.read_csv("maintext.csv")
for i, r in text.iterrows():
    if int(r.bold) == 1:
        st.write('**' + r['text'] + '**')
    else:
        r['text']

vr, li = st.columns(2)
with vr: 
    st.link_button(label="View Resume", url="https://drive.google.com/file/d/1PZITyUveKkRhnSGk_mbv2r8SYaXlOCrY/view?usp=sharing")
with li:
    st.link_button(label="LinkedIn", url="https://linkedin.com/in/sumedh-garimella")
st.text("Last Updated: January 2025")

# st.image('hdemusg.png', width=400)

with st.expander("Tech Stack of this page"):
    st.text("Language: Python")
    st.text("Libraries: Streamlit, Pandas, Base64")