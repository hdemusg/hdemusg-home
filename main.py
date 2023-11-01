import streamlit as st
import pandas as pd
import base64

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Abel&family=Barlow:wght@300&family=Didact+Gothic&display=swap');

			html, body, [class*="css"]  {
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

with open("static/resume.pdf", "rb") as f:
    pdf = f.read()
    b64pdf = base64.b64encode(pdf).decode("utf-8")
    st.download_button(label="Download Resume", data=pdf, file_name="SumedhG_resume.pdf", mime='application/octet-stream')
st.link_button(label="View Resume", url="https://drive.google.com/file/d/1c26ToeDj3YrYxgBprsTj3E-S3Rbqsjej/view?usp=sharing")

st.image('hdemusg.png', width=400)

with st.expander("Tech Stack of this page"):
    st.text("Language: Python")
    st.text("Libraries: Streamlit, Pandas, Base64")