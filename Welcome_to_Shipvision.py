import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Welcome to ShipVision",
    page_icon="",
)


# Add an emoji to the sidebar header
st.sidebar.header("🌟 Welcome to ShipVision")



st.title("Ship Detection in Satellite Images")

st.write("ShipVision is an AI-based tool to detect ships on satellite imagery. Our algorithm has been trained on thousands of real-life satellite images.")
st.write("On this website, you can try our algorithm in 2 different ways.")
st.write(" First, you can feed small individual images to our algorithm, and it will tell you whether the image contains a ship.")
st.write("Second, you can feed a 'large' satellite image (such as the image here below) to our model, it will identify all the ships on the image.")


# Load the image using PIL
image = Image.open('media/sfbay_3.png')

# Display the image with a specific width
st.image(image, caption='San Francisco Bay - Satellite Image', width=800)  # Adjust the width as needed
