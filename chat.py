import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os
import google.generativeai as genai

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/3dffcec0-9580-4675-be95-ddd7e09834a7/YMQN5pO39Q.json"


# Configure Google API
GOOGLE_API_KEY = "API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

def chat():
    # Function to load Gemini Pro model and get responses
    model = genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])

    def get_gemini_response(question):
        response = chat.send_message(question, stream=True)
        return response

    # Initialize Streamlit app
    st.title("Chat with Me!!")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Step into a realm of enriching dialogue where every interaction is an opportunity for discovery. Our platform offers a gateway to insightful conversations, where your inquiries are met with intelligent responses tailored precisely to your needs. Seamlessly integrated within our web interface, this immersive experience ensures effortless engagement and seamless exploration.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Chatbot***")
            st.write("Input Your Questions: Start by typing your questions in the text input field available in the main content area of our platform.")
            st.markdown("Request a Response: Once you've entered your question, simply click on the `Ask` button to send it off to our advanced AI processing system.")
            st.write("View Real-Time Responses: Upon submission, our chatbot swiftly generates a response tailored to your query. Watch as the response appears below the input field, providing you with immediate feedback.")
            st.markdown("Explore Your Chat History: Optionally, delve into your past conversations by accessing the chat history located on the sidebar. This feature allows you to review previous exchanges with the chatbot.")
            st.write("Experiment and Discover: Feel free to experiment with various questions and topics to explore the full capabilities of our conversational AI. Engage in meaningful discussions and uncover valuable insights along the way.")
            st.write("With these instructions at your fingertips, you're well-equipped to embark on an engaging journey of conversation and discovery with our conversational AI interface!")

    with col2:
        st_lottie(l1)


    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Sidebar
    st.sidebar.title("Instructions")
    st.sidebar.markdown(
        "1. Input your question in the text box below.\n"
        "2. Click on the 'Ask' button to get a response.\n"
        "3. View chat history on the right side."
    )

    # Main content area
    input_text = st.text_input("Input your question:", key="input")
    submit_button = st.button("Ask")

    if submit_button and input_text:
        response = get_gemini_response(input_text)
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

    # # Chat history
    # st.sidebar.title("Chat History")
    # chat_history = st.sidebar.empty()
    # for role, text in st.session_state['chat_history']:
    #     chat_history.write(f"**{role}:** {text}")

    # Apply some styling
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
            }
            .sidebar .sidebar-content .block-container {
                padding: 0px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
