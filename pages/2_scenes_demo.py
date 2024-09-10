import streamlit as st
import requests
from PIL import Image, ImageDraw
import io
import time


st.set_page_config(page_title="Scenes Demo", page_icon="!")
st.sidebar.header("Scenes Demo")
# Create a space title with 2 columns
col_icone, col_title = st.columns([1, 5])  # ratio to set the distance between the title and logo

# Display the image in front of the title
with col_icone:
    image_path = 'media/ship_vision.png'
    st.image(image_path, width=120)

with col_title:
    st.title("Ship Detection in Satellite Images")

st.write("Upload an image, review it, and then submit it to check if it contains a ship")

uploaded_file = st.file_uploader("Please, load an image...", type=["jpg", "jpeg", "png"])

# When the user clicks the button to submit for prediction
if uploaded_file is not None:
    # Load the image using PIL
    image = Image.open(uploaded_file)

    # Display the image for user confirmation
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # When the user clicks the button to submit for prediction
    if st.button("Submit for Prediction"):
        # Convert the image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()

 
        api_url = "https://shipvision-647806685234.europe-west1.run.app/predict-image"
 
        #api_url = "http://127.0.0.1:8000/predict-image"
 

        # Initialize progress bar
        progress_text = "Connecting to API..."
        my_bar = st.progress(0, text=progress_text)

        try:
            # Start measuring time for API request
            start_time = time.perf_counter()

            files = {"file": img_bytes}

            # Simulate a progress bar for the API request
            for percent_complete in range(1, 71):  # Phase 1: API request takes up to 70% progress
                time.sleep(0.05)  # Simulating time delay
                my_bar.progress(percent_complete, text=progress_text)

            # Send the request to the API
            response = requests.post(api_url, files=files)

            # Measure elapsed time for API request
            elapsed_time = time.perf_counter() - start_time

            # Check if the request was successful
            if response.status_code == 200:
                # Update progress bar to 70% after API call
                my_bar.progress(70, text="API Response Received. Processing Image...")

                # Extract the prediction from the API response
                response_json = response.json()

                coordinates = response_json['coordinates']
                predictions = response_json['predictions']

                draw = ImageDraw.Draw(image)
                patch_size = 80

                # Phase 2: Progress for drawing rectangles
                num_patches = len(predictions)
                for idx, prediction in enumerate(predictions):
                    # Update progress for each patch processed (from 71% to 100%)
                    progress_percentage = 70 + int((idx + 1) / num_patches * 30)
                    my_bar.progress(progress_percentage, text=f"Drawing Rectangles... {progress_percentage}%")

                    # Draw rectangles for patches classified as containing a ship
                    if prediction[0] > 0.7:
                        x, y = coordinates[idx]
                        draw.rectangle([x, y, x + patch_size, y + patch_size], outline='red', width=2)

                # Show the image with rectangles
                st.image(image, caption='Predicted Image', use_column_width=True)

                # Finish the progress bar after the loop
                my_bar.progress(100, text="Completed")

            else:
                st.error("Error: API response was not successful")

        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to the API. Details: {e}")
