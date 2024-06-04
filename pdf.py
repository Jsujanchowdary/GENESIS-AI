import streamlit as st
from streamlit_lottie import st_lottie
import requests
# from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplate import css, bot_template, user_template
from langchain.llms import HuggingFaceHub


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/dfa2260c-7c80-4671-8bb5-fd853f9c5f37/81mapnwT5f.json"

api_key = "API KEY"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    openai_api_key = api_key
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    openai_api_key = api_key
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def pdf():
    # load_dotenv()
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.title("PDF's Data Analysis Chatbot")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Unlock the potential of PDF documents with our advanced analysis capabilities. Seamlessly engage with AI-powered chatbots trained specifically on PDF content. Effortlessly extract actionable insights and gain a deeper understanding of your documents like never before.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for PDF Data Analysis***")
            st.write("Upload Your PDF Files: Start by uploading your PDF documents using the provided file uploader.")
            st.write("Select Your Document: After uploading, select the PDF document you wish to analyze from the dropdown menu.")
            st.write("Extract Text: Once selected, the platform will extract text from the PDF document and display it for analysis.")
            st.write("Interact with AI Chatbot: Engage with an AI-powered chatbot trained on the content of the PDF document. Ask questions, seek explanations, or request summaries to gain deeper insights.")
            st.write("Analyze Document Content: Utilize the chatbot's responses and the extracted text to analyze the content of the PDF document. Identify key points, trends, or patterns to inform your analysis.")
            st.write("Extract Insights: Extract actionable insights from the document content and the chatbot interactions. Use these insights to make informed decisions or guide further exploration.")
            st.write("Iterate and Explore: Experiment with different questions and analysis approaches to uncover hidden insights within the PDF document. Iterate as needed to refine your analysis and extract valuable knowledge.")
            st.write("With these instructions, you're equipped to leverage the power of AI for seamless PDF data analysis. Let's unlock the secrets hidden within your documents!")

    with col2:
        st_lottie(l1)
    user_question = st.text_input("Ask a question about your documents")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)
                