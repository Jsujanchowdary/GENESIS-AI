import streamlit as st
from streamlit_lottie import st_lottie
from pandasai.llm.openai import OpenAI
from dotenv import load_dotenv
import requests
import os
import pandas as pd
from pandasai import SmartDataframe
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/2f7cf9a0-3475-430c-87c7-1664b5e17660/GUdpy07yaC.json"



openai_api_key ="API KEY"

def chat_with_csv(df,prompt):
    llm = OpenAI(api_token=openai_api_key)
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    return result

def csv():
    st.header("DATA ANALYSIS WITH CSV DATA")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Delve into CSV Data Analysis: Seamlessly explore and interpret your CSV datasets. Engage in intuitive data interrogation using natural language queries, unlocking instant insights and dynamic visualizations to facilitate informed decision-making.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for CSV Data Analysis***")
            st.write("Upload Your CSV Files: Get started by uploading your CSV files using the provided file uploader.")
            st.write("Select Your Dataset: Once uploaded, choose the CSV file you wish to analyze from the dropdown menu.")
            st.write("Visualize Your Data: Upon selection, your dataset will be displayed in a tabular format. Utilize the interactive controls to delve deeper into your data and visualize key insights.")
            st.markdown("Pose Your Queries: Use the text input field to ask natural language questions about your data. For instance, inquire about trends or averages such as `What are the sales trends?` or `What is the average revenue?`")
            st.write("Analyze Your Results: Instantly receive insights and visualizations tailored to your query. Dive into the provided results to gain a comprehensive understanding of your dataset.")
            st.write("Iterate and Explore: Experiment with different queries and visualizations to uncover valuable patterns, trends, and anomalies. Iterate as needed to refine your analysis and extract actionable insights.")
            st.write("With these instructions, you're ready to harness the power of AI for seamless CSV data analysis. Lets explore yourdata together!")

    with col2:
        st_lottie(l1)

    # Upload multiple CSV files
    input_csvs = st.file_uploader("Upload your CSV files", type=['csv'], accept_multiple_files=True)

    if input_csvs:
        # Select a CSV file from the uploaded files using a dropdown menu
        selected_file = st.selectbox("Select a CSV file", [file.name for file in input_csvs])
        selected_index = [file.name for file in input_csvs].index(selected_file)

        #load and display the selected csv file 
        st.info("CSV uploaded successfully")
        data = pd.read_csv(input_csvs[selected_index])
        st.dataframe(data,use_container_width=True)

        #Enter the query for analysis
        st.info("Chat Below")
        input_text = st.text_area("Enter the query")

        #Perform analysis
        if st.button("Chat with csv"):
            if input_text:
                st.info("Your Query: "+ input_text)
                result = chat_with_csv(data,input_text)
                fig_number = plt.get_fignums()
                if fig_number:
                    st.pyplot(plt.gcf())
                else:
                    st.success(result)