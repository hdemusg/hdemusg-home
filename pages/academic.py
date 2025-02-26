import streamlit as st
import base64

st.set_page_config(page_title="Sumedh Surya Garimella | Academic", page_icon=":ledger:")

streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Abel&family=Barlow:wght@300&family=Didact+Gothic&display=swap');

			* {
			font-family: 'Abel', sans-serif;
			}
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

st.header('Academic Experience')

'''I graduated from the Georgia Institute of Technology in 2022 with my B.S. in Computer Science, 
        and remained in Atlanta for another year to complete my M.S. in Computer Science.'''

tabs = ["MS Computer Science - Georgia Tech",
        "BS Computer Science - Georgia Tech",
        "Peachtree Ridge HS"]

m, b, h, c = st.tabs(tabs)

with m:
    with st.expander("Overview"):
        st.metric("Start Date", "August 2022")
        st.metric("End Date", "May 2023")
        st.metric("GPA", 3.67)
    
    ma, mb, mc = st.tabs(['Coursework', 'Extracurricular', 'Projects'])
    with ma:
        st.write(
        '''
        **Relevant coursework:** \n
            - Computer Vision \n
            - Robot Intelligence: Planning \n
            - Interactive Robot Learning \n
            - Data Science for Epidemiology \n
            - Machine Learning for Computational Biology \n
            - Game AI \n
            - Ubiquitous Computing \n
        '''
        )
        
    with mb: 
        '''
        **Graduate Teaching Assistant, Intro to AI (Jan 2022 - May 2023):** \n
            - Held office hours and graded exams \n
            - Presented lectures on AI in the medical field \n

        **Radio Operator/DJ, WREK Radio (Feb 2022 - April 2023):** \n
            - Operated FM 91.1 (WREK Atlanta) for 1 hour a week, playing topical music, managing contests, and announcing PSAs \n
            - Trained 3 freshmen to become radio operators \n
            - Managed sound and audio for events across campus \n
        '''
    with mc:
        '''
        **Dog Project, Mobile and Ubiquitous Computing (Spring 2023):** \n
            - Processed 20+ minutes of audio from dogs in a lab environment to create spectrograms for classification.
            - Implemented a supervised MLP model for classifying of toy squeaks for determining dog stress.
        
        **Natural Disasters + COVID, Data Science for Epidemiology (Fall 2022):** \n
            - Combined Apple mobility and NYT COVID datasets to determine effect to which natural disaster evacuations contributed to COVID rates in affected and neighboring states.
        '''

with b:
    with st.expander("Overview"):
        st.metric("Start Date", "August 2018")
        st.metric("End Date", "May 2022")
        st.metric("GPA", 3.74)
    ba, bb, bc = st.tabs(['Coursework', 'Extracurricular', 'Projects'])
    with ba:
        '''
        **Relevant coursework:** \n
            - Machine Learning \n
            - Robotics and Perception \n
            - Natural Language Processing \n
            - Intro to AI
        '''
    with bb: 
        '''
        **Senior Teaching Assistant, Objects and Design (Jan 2022 - May 2023):** \n
            - Built a website (used by over 1000+ students) for course materials and practice exam questions. \n
            - Managed a team of 6 other TAs to develop and release regular updates to the content and structure of the website. \n
        '''
    with bc:
        '''
        **Voilo (August 2019 - January 2020):** \n
            - Built an application to store text-based reminders with coordinates to help people remember where they parked.
            - Used Google Maps API to provide walking directions to reminder locations.
            - Created an alpha test program with 5 people to determine necessary improvements.
        '''

with h:
    with st.expander("Overview"):
        st.metric("Start Date", "August 2014")
        st.metric("End Date", "May 2018")
    ba, bb= st.tabs(['Coursework', 'Extracurricular'])
    with ba:
        '''
        **Relevant coursework:** \n
            - AP Computer Science \n
            - Linear Algebra (Georgia Tech) \n
            - Multivariable Calculus (Georgia Tech) \n
            - Differential Equations \n
        '''
    with bb: 
        '''
        **VP of Membership, Peachtree Ridge FBLA (Future Business Leaders of America):** \n
            - Developed website for members to keep up to date with chapter meetings and deadlines. \n
            - Managed member data and dues payments for over 100+ chapter members.

        **Programming Lead, FRC Team 1261**
            - Trained 10+ freshmen in Java fundamentals.
            - Managed the development of software for 2 functioning competitive robots.
            - Designed the autonomous functionality of said robots.
        '''
    
with c:
    with st.expander("Certifications"):
        st.write("MongoDB SI Associate, Capgemini L0 Architect, Databricks Apache Spark for Data Scientists")

    