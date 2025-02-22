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

with st.expander("Data Scientist at Capgemini"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "New York, NY")
    with t:
        st.metric("Start Date", "December 2023")

    tabs = ["Client Work", "Internal Work"]
    cw, iw = st.tabs(tabs)
    with cw:
        st.text("""Minimized annual product onboarding-related manual labor costs for an international grocery chain by up to $1 million by architecting an Azure Functions pipeline connecting product image storage, a label detection model, GPT-4o, and Azure SQL. \n
Trained multiple iterations of the underlying bounding box model on sample images using Azure ML to increase OCR accuracy by 20%. \n
Engineered an algorithm based on Normalized Levenshtein similarity for evaluating LLM prompt performance. \n
Built reusable Python components (for data ingestion and vectorization of structured and unstructured data) to facilitate quicker development of AI applications in Databricks.  """)
    with iw:
        st.text("""
Built an automated Python QA workflow to reconcile discrepancies between practice-wide pipeline reports. \n
Built a Streamlit application to retrieve internal PowerPoint decks relevant to a user query with RAG.""")

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
        st.text("""Deployed REST API endpoints for ETL of transaction data from a cash management app to BigQuery. Performed QA and integration testing using SQL queries to ensure errorless data transfer and data integrity.""")
    with nb:
        st.text("""Evangelized Go adoption company-wide by releasing a Go module with miscellaneous mathematical and
scientific functions, including Markov Chains.""")
        # add a button linking to github
        st.link_button(label="Gophourri", url="https://github.com/hdemusg/gophourri")
    with nc: 
        st.text("""Built the MongoDB database and designed the schema for user records for a computer vision application for autoverifying IDs in self-checkouts.""")
    
with st.expander("Global Technology Summer Analyst (Data Science Intern) at Bank of America"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Remote")
    with t:
        st.metric("Start Date", "June 2021")
        st.metric("End Date", "August 2021")
    ba = st.tabs(["Main Responsibilities"])
    with ba:
        st.text("""
        Used NLP techniques to classify confidential and proprietary documents for data governance purpose. 
        Built data pipelines for information extraction of relevant text from multiple file types for storage in SQLite. 
        Performed daily data quality checks in SQL and Excel on millions of rows of internal data to ensure compliance.
        Designed a procedure for optimization of data entry via automation of data check summarization.
        """)
    
with st.expander("R&D Innovation Intern at Coca-Cola"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Atlanta, GA")
    with t:
        st.metric("Start Date", "May 2019")
        st.metric("End Date", "August 2019")
    ca, cb = st.tabs(["R&D Digitization", "NLP Experimentation"])
    with ca:
        st.text("Digitized ingredient decision-making workflows of research scientists by building an Azure-hosted website.")
    with cb:
        st.text("Utilized word2vec and doc2vec algorithms on social media data to predict consumer tastes with an accuracy of 75%.")

with st.expander("IT Innovation Intern at ZF North America"):
    l, t = st.columns(2)
    with l:
        st.metric("Location", "Gainesville, GA")
    with t:
        st.metric("Start Date", "June 2017")
        st.metric("End Date", "July 2017")
    za = st.tabs(["R&D Digitization"])
    with za:
        st.text("Contributed to the development of a delivery planning system in Python.")