from flask import Flask, request, jsonify
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from dotenv import load_dotenv
import os
import torch

app = Flask(__name__)

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# @app.route('/api/hello', methods=['GET'])
# def hello_world():
#     return jsonify(message="Hello", test=os.getenv('SECRET_KEY'))
# this is feature branch  dfdfdf

@app.route('/api/generate_caption', methods=['POST'])
def generate_caption():
    if 'image' not in request.files:
        return jsonify(error="No image file provided"), 400

    image_file = request.files['image']
    image = Image.open(image_file).convert("RGB")

    inputs = processor(image, return_tensors="pt").to(model.device)
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    return jsonify(caption=caption)

if __name__ == '__main__':
    app.run(debug=True)