import streamlit as st
import requests
from PIL import Image
import io

st.title("Ship Detection in Satellite Images")


st.write("Upload an image, review it, and then submit it to check if it contains a ship")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    image = Image.open(uploaded_file)
    # st.image(image, caption='Uploaded Imagee', use_column_width=True)


    if st.button("Submit for Prediction"):
        # Convert the image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')  # Use PNG or the appropriate format
        img_bytes = img_bytes.getvalue()

        # Define your API endpoint
        api_url = "https://example.com/predict"  # Replace with your actual API URL

        # Send the image to the API
        try:
            response = requests.post(
                api_url,
                files={"file": ("uploaded_image.png", img_bytes, "image/png")}
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Extract the prediction from the API response
                result = response.json().get('prediction', 'No prediction found')
                st.success(f"Prediction: **{result}**")
            else:
                st.error(f"Error: API returned status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to the API. Details: {e}")
