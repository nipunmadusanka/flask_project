from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello", test=os.getenv('SECRET_KEY'))

if __name__ == '__main__':
    app.run(debug=True)