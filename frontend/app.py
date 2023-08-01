import streamlit as st
import requests
from PIL import Image
import io
import numpy as np

# Set the server URL (change this to your actual URL)
SERVER_URL = 'http://backend:8000/get_prediction'

# Create a sidebar for uploading the image
st.sidebar.header('Upload an Image')
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Convert the file to an image
    image = Image.open(uploaded_file)

    # Create two columns for displaying the images
    col1, col2 = st.columns(2)

    # Display the uploaded image in the first column
    col1.image(image, caption='Uploaded Image', use_column_width=True)

    if st.sidebar.button('Predict'):
        # Convert the image to bytes
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_bytes = buffered.getvalue()

        # Send the image to the server and get the prediction
        response = requests.post(SERVER_URL, files={"file": ("image.jpg", img_bytes)})
        data = response.json()
        annotated_img = data["annotated_img"]

        # Convert the nested list (2D list) to a numpy array
        numpy_image = np.array(annotated_img).astype("uint8")

        # Convert the BGR image to RGB
        rgb_image = numpy_image[..., ::-1]

        # Display the prediction in the second column
        col2.image(rgb_image, caption='Annotated Image', use_column_width=True)
