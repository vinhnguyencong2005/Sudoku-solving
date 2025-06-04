from google import genai
from PIL import Image
import pathlib
import base64

# Initialize the client
client = genai.Client(api_key="Your-api-key")  # Replace with secure method!

# Path to your image
text_prompt = "Sorry to borthering you, please answer me only the grid of the sudoku game, say nothing more. The output format with no space for example:\n" + "|1|2|3|4|7|n|n|n|n|" + "|2|n|n|n|n|n|n|n|n|\n" +  "|3|n|n|n|n|n|n|n|n|\n" + "|4|n|n|n|n|n|n|n|n|\n" + "|5|n|n|n|n|n|n|n|n|\n" + "|6|n|n|n|n|n|n|n|n|\n" + "|7|n|n|n|n|n|n|n|n|\n" + "|8|n|n|n|n|n|n|n|n|\n" + "|9|n|n|n|n|n|n|n|n|\n" + "If not thing there, put n there. No gap between them, only '|' there"  # e.g.,"C:/Users/summo/Data/image.jpg"

# Your text prompt
image_path = input("Enter the path to your image: ")

# Load the image to verify it exists
image = Image.open(image_path)

# Read and encode the image properly
with open(image_path, "rb") as img_file:
    image_bytes = img_file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

# Create a multipart prompt with both text and image
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=[
        {"role": "user", "parts": [
            {"text": text_prompt},
            {"inline_data": {
                "mime_type": image.get_format_mimetype(),  # Get correct mime type automatically
                "data": image_base64
            }}
        ]}
    ]
)

print(response.text)