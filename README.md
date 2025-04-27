# Image Caption Generator API

A Flask-based REST API that generates captions for images using the BLIP (Bootstrapping Language-Image Pre-training) model from Hugging Face.

## Description

This API allows users to upload an image and receive an automatically generated caption that describes the content of the image. It uses the `Salesforce/blip-image-captioning-base` model from Hugging Face's transformers library.

## Features

- Image caption generation via REST API
- Built with Flask
- Powered by BLIP model from Hugging Face

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   
   # Additional dependencies not in requirements.txt
   pip install torch transformers pillow
   ```

4. Create a `.env` file in the root directory (optional for environment variables)

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

## API Endpoints

### Generate Caption

**Endpoint:** `/api/generate_caption`

**Method:** POST

**Content-Type:** multipart/form-data

**Parameters:**
- `image`: The image file to generate a caption for

**Response:**
```json
{
  "caption": "a person riding a surfboard on a wave"
}
```

**Error Response:**
```json
{
  "error": "No image file provided"
}
```

## Example Usage

Using curl:
```bash
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5000/api/generate_caption
```

Using Python requests:
```python
import requests

url = "http://localhost:5000/api/generate_caption"
files = {"image": open("path/to/your/image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

## Dependencies

- Flask: Web framework
- Transformers: For the BLIP model
- PyTorch: Required by Transformers
- Pillow: For image processing
- python-dotenv: For loading environment variables

## License

--

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the BLIP model
- [Salesforce](https://www.salesforce.com/) for developing the BLIP model
