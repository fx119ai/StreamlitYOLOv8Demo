import requests
from PIL import Image
import io
import cv2
import numpy as np
import argparse
from utils import file_exists, parent_folder_exists, valid_image_type


parser = argparse.ArgumentParser(description='YOLOv8 pose estimation.')
parser.add_argument('--input-path', required=True, help='Path to the input image')
parser.add_argument('--output-path', required=True, help='Path to the output image')
parser.add_argument('--show', type=bool, default=False, help='Show the image after processing')

args = parser.parse_args()

print(f'Input path: {args.input_path}')
print(f'Output path: {args.output_path}')
print(f'Show: {args.show}')

# A few sanity checks
file_exists(args.input_path)
parent_folder_exists(args.output_path)
valid_image_type(args.input_path)

# Load the image
image = Image.open(args.input_path)

# Convert the image to bytes
img_byte_arr = io.BytesIO()
image.save(img_byte_arr, format='JPEG')
img_byte_arr = img_byte_arr.getvalue()

# Make the POST request
response = requests.post(
    "http://localhost:8000/get_prediction",
    files={"file": ("image.jpg", img_byte_arr)},
)

# Print the response
if response.status_code == 200:
    data = response.json()
    annotated_img = data["annotated_img"]
    annotated_img_processed = np.asarray(annotated_img).astype("uint8")
    if args.show:
        cv2.imshow("YOLOv8 Inference", annotated_img_processed)
        cv2.waitKey()
    cv2.imwrite(args.output_path, annotated_img_processed)
else:
    print(f"Request failed with status code {response.status_code}")