import streamlit as st
from streamlit_lottie import st_lottie
import requests


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/913b6a51-e61d-45c6-b2fb-80723fe7171f/NzKkcY1mUv.json"
l2 = "https://lottie.host/2faac3d2-56d8-4471-8df1-bb56bf6fb799/ff9lxre1nU.json"
l3 = "https://lottie.host/11d7731c-f8f7-45ff-89d7-c7c11d980efd/ilMGdhHEoe.json"
l4 = "https://lottie.host/ca361236-4c82-4523-927a-69683924fe33/Udz13lEk8r.json"
l5 = "https://lottie.host/05b244e7-3c08-4440-b3d1-9c3d656cada0/uZ4x2KXm1v.json"
l6 = "https://lottie.host/6802bb15-0d2e-4b0a-af28-32c0b8c4c31a/TKMi9L7zkK.json"
l7 = "https://lottie.host/4f47e133-f8b8-4eab-bd9e-b4ee759f90ea/ZWkQwQyPsW.json"
l8 = "https://lottie.host/33f81951-c5a3-4a57-a9f2-cbdd81fa8119/pdDzXH4HdU.json"

def about():
    col1, col2 = st.columns(2)
    with col1:
        st.title("Know About Us!!")
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.subheader("Welcome to AI Powered Data Analysis Chatbot, an innovative platform that harnesses the power of AI to revolutionize data analysis and interaction. Our project combines cutting-edge technologies to deliver seamless experiences for analyzing PDF and CSV data, identifying objects in images, and engaging in natural language conversations.")
    with col2:
        st_lottie(l1)
    st.write("---")
    col3, col4 = st.columns(2)
    with col3:
        st_lottie(l2)
    with col4:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Our Mission")
        st.subheader("Empowering individuals and organizations with innovative AI technologies to unlock valuable insights from their data effortlessly and efficiently. Driven by our passion for technology and our commitment to delivering unparalleled value, we strive to:")
        st.markdown("- **Empower**: Empower individuals and organizations with the tools and insights needed to make informed decisions and drive meaningful outcomes.")
        st.markdown("- **Innovate**: Continuously innovate and push the boundaries of what is possible, leveraging the latest advancements in AI and data analysis to stay ahead of the curve.")
        st.markdown("- **Simplify**: Simplify the complexities of data analysis and interaction, making advanced technologies accessible and user-friendly for everyone.")

    st.write("---")
    col9, col10 = st.columns(2)
    with col9:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Our Commitment to Excellence")
        st.subheader("At Genesis AI, we are dedicated to delivering excellence in every aspect of our service. From cutting-edge AI technologies to intuitive user interfaces, we strive to provide a seamless and unparalleled experience for our users.")
    with col10:
        st_lottie(l7)
    st.write("---")
    col11, col12 = st.columns(2)
    with col11:
        st_lottie(l8)
    with col12:
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.title("Data-driven Innovation")
        st.subheader("We believe in the power of data to drive innovation and transformation. Our platform empowers individuals and organizations to harness the full potential of their data, enabling them to make informed decisions and unlock new opportunities for growth.")
    # Add footer with CSS for fixed positioning
    st.write("---")
    st.title("Explore Our Advanced Features")
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st_lottie(l3)
        st.write("PDF Data Analysis")
        st.write("Analyze PDF documents with precision. Engage with an AI-powered chatbot trained on PDF content. Extract actionable insights and knowledge from textual data effortlessly.") 

    with col6:
        st_lottie(l4)
        st.write("CSV Data Analysis")
        st.write("Visualize and analyze CSV data with ease.Pose natural language queries for data exploration.Access instant insights and visualizations to drive informed decisions.")

    with col7:
        st_lottie(l5)
        st.write("Object Data Analysis")
        st.write("Harness state-of-the-art object detection algorithms.Identify objects within images accurately and efficiently.Simplify image analysis and object recognition tasks.")

    with col8:
        st_lottie(l6)
        st.write("Conversational AI")
        st.write("Engage in insightful conversations powered by AI. Receive intelligent responses tailored to your inquiries. Experience seamless interaction and communication for enhanced productivity.")

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

# You can then call the about function in your main app.py file
