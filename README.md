# Egonym Coding Challenge

## Assignment
- Pick any of the pretrained YOLOv8 models from [1] and set up a backend infrastructure that serves the prediction functionality through a REST API.
- Optionally, you can create a minimalistic WebUI that facilitates the upload of an image and displays the return value and data.
- Running the server on localhost is sufficient enough, but it is also allowed to deploy it somewhere on cloud.

## Solution
I decided to go with using fastapi as my backend framework and streamlit as a quick prototyping frontend. For easy usability 
I used docker-compose having one docker container that runs the backend and one that runs the frontend. 

## How to

### Version 1 - Streamlit

1. Go to the project route and execute the following two commands one after the other:
    - `docker-compose build`
    - `docker compose up`
2. Once those ran successfully open the streamlit app through `http://localhost:8501` in your browser
3. You can then upload an image and once the image is uploaded make a prediction by using the predict button


### Version 2 - command line
1. Install the vritualenv package on your machine with `pip3 install virtualenv`
2. Create a virtual environment in the project route with `virtualenv venv`
3. Activate the environment with `source venv/bin/activate`
4. Install all the required packages with `pip install -r requirements.txt`
5. Execute the following two commands one after the other:
    - `docker-compose build` (only if not built yet)
    - `docker-compose up backend`
6. Call the backend like the following: `python get_prediction.py --input-path backend/data/test2.jpg --output-path backend/data/test2_annotated.jpg --show True` 
-> the code assumes that the folders and files exist, but it would also be

