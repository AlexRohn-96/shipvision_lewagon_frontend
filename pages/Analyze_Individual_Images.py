import streamlit as st
import requests
from PIL import Image


st.set_page_config(page_title="Analyze Individual Images", page_icon="!")
st.sidebar.header("🚢 Analyze Individual Images")


st.title("Detect Ships on Invididual Images")


st.write("Upload a small image, and press on submit, our model will tell you if it contains a ship.")

uploaded_file = st.file_uploader("Please, load an image...", type=["jpg", "jpeg", "png"])

    # When the user clicks the button to submit for prediction
        # When the user clicks the button to submit for prediction
if uploaded_file is not None:
    # Load the image using PIL
    image = Image.open(uploaded_file)

    # Ensure the image is in RGB format (in case it's a grayscale image)
    image = image.convert('RGB')

    # Resize the image to 80x80 pixels
    image = image.resize((80, 80))

    # Display the resized image for user confirmation
    st.image(image, caption='Resized Image (80x80)', use_column_width=True)

    # When the user clicks the button to submit for prediction
    if st.button("Submit"):
        # Separate the red, green, and blue channels into their own lists
        red_channel = []
        green_channel = []
        blue_channel = []

        for pixel in image.getdata():
            r, g, b = pixel
            red_channel.append(r)
            green_channel.append(g)
            blue_channel.append(b)


        pixel_values = red_channel + green_channel + blue_channel


        # api_url = "http://127.0.0.1:8000/predict"  # Replace with your actual API URL


        api_url = "https://shipvision-647806685234.europe-west1.run.app/predict"  # Replace with your actual API URL

        # Send the list of pixel values to the API as JSON (POST request)
        try:
            # params = {"X": pixel_values}  # Assuming pixel_values is simple and can be passed as a string
            # response = requests.get(api_url, params=params)
            response = requests.post(
                api_url,
                json={"X": pixel_values}  # Send the normalized pixel list as JSON
            )


            # Check if the request was successful
            if response.status_code == 200:
                # breakpoint()
                # Extract the prediction from the API response
                result = response.json().get('Prediction', 'No prediction found')
            else:
                st.error(f"Error: API returned status code {response.status_code}")

            if result==1:
                # Display the SHIP message in green and large font
                st.markdown(
                    "<h2 style='color:green;'>SHIP: According to our model, this image contains a ship.</h2>",
                    unsafe_allow_html=True
                )

            if  result==0:
                # Display the NO SHIP message in red and large font
                st.markdown(
                    "<h2 style='color:red;'>NO SHIP: According to our model, this image does NOT contain a ship.</h2>",
                    unsafe_allow_html=True
                )


        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to the API. Details: {e}")
