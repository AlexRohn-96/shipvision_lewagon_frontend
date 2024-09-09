import streamlit as st
import requests
from PIL import Image




# create a space title with 2 columns
col_icone, col_title = st.columns([1, 5]) #ratio to set the distance between the title and logo
# display the image in front of the title
with col_icone:
    image_path='/home/olivierpi/code/AlexRohn-96/shipvision_lewagon_frontend/media/ship_vision.png'
    st.image(image_path,width=120)

with col_title:
    st.title("Ship Detection in Satellite Images")


st.write("Upload an image, review it, and then submit it to check if it contains a ship")

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
    if st.button("Submit for Prediction"):
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





        #pixel_values = [0, 128, 255]

        # Define your API endpoint
        api_url = "http://127.0.0.1:8000/predict"  # Replace with your actual API URL
        #api_url = "https://shipvision-83086093480.europe-west1.run.app/predict"  # Replace with your actual API URL
        #https://shipvision-647806685234.europe-west1.run.app/
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
                st.success(f"Prediction: **{result}**. There is a ship inside this picture")

            if  result==0:
                st.success(f"Prediction: **{result}**. There is no ship inside this picture")


        except requests.exceptions.RequestException as e:
            st.error(f"Error: Could not connect to the API. Details: {e}")
