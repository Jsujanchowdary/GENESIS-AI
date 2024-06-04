import streamlit as st
from PIL import Image
import os
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

l1 = "https://lottie.host/3244e710-2470-4ade-8d4f-2654e645be11/loLAddQjXP.json"


GOOGLE_API_KEY = "API KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}


def object_det():
    st.title("Object Finder 🔍")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(" ")
        st.subheader(" ")
        st.subheader(" ")
        st.subheader("Our platform leverages cutting-edge object detection technology to analyze images and identify objects within them. Whether you're exploring images for research, education, or curiosity, our tool provides accurate and efficient object detection capabilities.")
        
        # Hide the disclaimer initially
        st.write("")

        # Show the disclaimer if the button is clicked
        with st.expander("Disclaimer ⚠️", expanded=False):
            st.markdown("***Instructions for Image Data Analysis***")
            st.write("Upload Your Image: Start by uploading an image containing the objects you want to identify. Use the file uploader to select an image from your device.")
            st.write("Explore Image Details: Once uploaded, the image will be displayed on the interface along with its dimensions. Take a moment to review the image details.")
            st.write("Pose Your Question: Optionally, input a question related to the image in the provided text input field. This can help contextualize the object detection process.")
            st.markdown("Initiate Object Detection: Click the `Identify the objects` button to initiate the object detection process. Our AI model will analyze the image and identify objects within it.")
            st.write("View Detected Objects: Upon completion, the identified objects will be listed on the interface. Explore the list to see which objects were detected.")
            st.write("Iterate and Explore: Experiment with different images and questions to explore the capabilities of our object detection tool. Iterate as needed to refine your analysis and gain insights from various images.")
            st.write("With these instructions, you're ready to utilize our Object Finder tool to analyze images and identify objects with ease. Let's uncover the secrets hidden within your images!")

    with col2:
        st_lottie(l1)

    disclaimer_message = """This is a object detector model so preferably use images containing different objects,tools... for best results 🙂"""

    # Hide the disclaimer initially
    st.write("")

    # Show the disclaimer if the button is clicked
    with st.expander("Disclaimer ⚠️", expanded=False):
       st.markdown(disclaimer_message)
    

    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Choose an image ...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

        # Process the image (example: get image dimensions)
        image = Image.open(uploaded_image)
        width, height = image.size
        st.write("Image Dimensions:", f"{width}x{height}")

        question = st.text_input("Question?")

        if st.button("Identify the objects"):

            st.success("Detecting...")

            vision_model = genai.GenerativeModel('gemini-pro-vision')
            response = vision_model.generate_content([question,image])

            
            st.write("The objects detected are \n", response.text)

            st.success("Thanks for visiting 🤩!!")



