import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Welcome to ShipVision",
    page_icon="",
)


# Add an emoji to the sidebar header
st.sidebar.header("🌟 Welcome to ShipVision")

def set_background_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #FFFFFF; /* White background color */
        }
        .title-container {
            display: flex;
            align-items: center;
            padding: 10px; /* Adjust padding as needed */
            justify-content: flex-start; /* Ensure items align to the left */
        }
        .title-container h1 {
            color: black; /* Ensure the title is black */
            margin: 0; /* Remove default margin */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_color()

# Create a container for the title
st.markdown(
    """
    <div class="title-container">
        <h1>Ship Detection in Satellite Images</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("ShipVision is an AI-based tool to detect ships on satellite imagery. Our algorithm has been trained on thousands of real-life satellite images.")
st.write("On this website, you can try our algorithm in 2 different ways.")
st.write(" First, you can feed small individual images to our algorithm, and it will tell you whether the image contains a ship.")
st.write("Second, you can feed a 'large' satellite image (such as the image here below) to our model, it will identify all the ships on the image.")


# Load the image using PIL
image = Image.open('media/sfbay_3.png')

# Display the image with a specific width
st.image(image, caption='San Francisco Bay - Satellite Image', width=800)  # Adjust the width as needed
