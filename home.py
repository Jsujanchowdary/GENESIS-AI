import streamlit as st
import os
from streamlit_lottie import st_lottie
import requests
from pdf import pdf
from csvdata import csv
from chat import chat
from pdfcontextbot import pdfcontextbot
from object_det import object_det

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/292055de-61e6-4874-91fa-d3e60e8f22a2/gDngCr7IHX.json"

def home():
    st.markdown("<h1 style='text-align: center; color: white;'>Discover the power of Genesis AI</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.header("")
        st.header("")
        st.header("")
        st.markdown("""
        <style>
        .big-font {
            font-size:100px !important;
        }
        .small-font{
            font-size: 20px !
        }
        .bold-text{
            font-weight: bold !important;
        }
        .text-ali{
            text-align: center
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<p class="big-font bold-text">Welcome to Genesis AI</p>', unsafe_allow_html=True)
        st.subheader("Your Intelligent Data Analysis Companion! 🤖")
        st.write("Have questions about your data? Need insightful analysis in seconds? You're in the right place!")

    with col2:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.image(r"..\LangChain_LLm_Data\images\home.png")

    st.write("---")
    
    st.markdown("<h1 style='text-align: center; color: white; font-size:35px;'>Ask Genesis AI anything about your PDF's, CSV or Image files. From trend analysis to contextual understanding, Genesis AI has got you covered.</h1>", unsafe_allow_html=True)
    #st.write("Simply upload your files and start chatting. Let's unlock the power of AI together! 💡")

    col3,col4,col5,col6 = st.columns(4)
    with col3:
        st.image(r"..\LangChain_LLm_Data\images\Untitled design (2).png")
    with col4:
        st.image(r"..\LangChain_LLm_Data\images\Untitled design (3).png")
    with col5:
        st.image(r"..\LangChain_LLm_Data\images\Untitled design (4).png")
    with col6:
        st.image(r"..\LangChain_LLm_Data\images\Untitled design (5).png")
    
    st.markdown("<h1 style='text-align: center; color: white; font-size:35px;'>Simply upload your files and start chatting. Let's unlock the power of AI together! 💡</h1>", unsafe_allow_html=True)
    st.write("---")

    col7,col8 = st.columns(2)
    with col7:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.header("Why Choose Genesis AI?")
        st.subheader("1. Instant Insights: Get actionable insights from your data in real-time.")
        st.subheader("2. Versatile Analysis: Analyze CSV, image, or PDF files effortlessly.")
        st.subheader("3. Conversational AI: Chat with Genesis AI to explore your data in a natural way.")
        st.subheader("4. User-Friendly: Easy-to-use interface for seamless interaction.")
        st.subheader("5. Powerful AI: Leveraging cutting-edge AI technology for accurate analysis.")

    with col8:
        st_lottie(l1)

    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 80%;
            background-color: #000000;
            text-align: center;
            padding: 10px 0;
        }
        </style>
        <div class="footer">
            Powered by Genesis AI ©️ 2024
        </div>
        """,
        unsafe_allow_html=True
    )


