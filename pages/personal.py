import streamlit as st

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
        '''
        Coming soon.
        '''
        
        

with i:
    st.subheader("Interests")
    with st.expander("Fly Montag (Music)"):
        st.link_button("Website", "https://flymontag-2767c.web.app")
        '''
        Technologies used for website: Firebase, Python Flask
        '''
    
