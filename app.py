import streamlit as st
import streamlit_option_menu as  option_menu
import os
from home import home
from about import about
from pdf import pdf
from csvdata import csv
from chat import chat
from pdfcontextbot import pdfcontextbot
from object_det import object_det



def main():
    st.set_page_config(layout='wide')
    st.sidebar.image(r"..\LangChain_LLm_Data\images\Cyan Modern Technology Logo.png")
    navigation = st.sidebar.selectbox("Menu", ["HOME","ABOUT","PDF DATA ANALYSIS","PDF CONTEXT CHAT BOT","CSV DATA ANALYSIS","OBJECT DATA ANALYSIS","CHAT WITH ME"])

    
    
    if navigation == "HOME":
        home()
    elif navigation == "ABOUT":
        about()
    elif navigation == "PDF DATA ANALYSIS":
        pdf()
    elif navigation == "PDF CONTEXT CHAT BOT":
        pdfcontextbot()
    elif navigation == "CSV DATA ANALYSIS":
        csv()
    elif navigation == "OBJECT DATA ANALYSIS":
        object_det()
    elif navigation == "CHAT WITH ME":
        chat()
    


if  __name__ == "__main__":
    main()

    