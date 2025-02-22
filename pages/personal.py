import streamlit as st

st.set_page_config(page_title="Sumedh Surya Garimella | Personal", page_icon=":rocket:")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Abel&family=Barlow:wght@300&family=Didact+Gothic&display=swap');

			*  {
			font-family: 'Abel', sans-serif;
			}
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.header("Personal Projects and Interests")

p, i = st.columns(2)
with p:
    st.subheader("Projects")
    with st.expander("K-Means Clustering Art Generator"):
        st.text("Coming soon")

with i:
    st.subheader("Interests")
    with st.expander("Fly Montag (Music)"):
        st.link_button("Website", "orca-app-7udhr.ondigitalocean.app")
        st.metric("Streams", 4000)
    
