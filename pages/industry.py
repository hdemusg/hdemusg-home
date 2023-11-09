import streamlit as st

st.set_page_config(page_title="Sumedh Surya Garimella | Industry", page_icon=":briefcase:")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Abel&family=Barlow:wght@300&family=Didact+Gothic&display=swap');

			* {
			font-family: 'Abel', sans-serif;
			}
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.header("Industry Experience")

with st.expander("Software Engineering Intern at NCR"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Atlanta, GA")
    with t:
        st.metric("Start Date", "May 2022")
        st.metric("End Date", "August 2022")

    tabs = ["Main Responsibilities", "Learning Go", "Hackathon"]
    na, nb, nc = st.tabs(tabs)
    with na:
        st.text("Main Task: Modernize Cash Office application")
    
with st.expander("Global Technology Summer Analyst (Data Science Intern) at Bank of America"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Remote")
    with t:
        st.metric("Start Date", "June 2021")
        st.metric("End Date", "August 2021")

    
    
with st.expander("R&D Innovation Intern at Coca-Cola"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Atlanta, GA")
    with t:
        st.metric("Start Date", "May 2019")
        st.metric("End Date", "August 2019")

with st.expander("IT Innovation Intern at ZF North America"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Gainesville, GA")
    with t:
        st.metric("Start Date", "June 2017")
        st.metric("End Date", "July 2017")
