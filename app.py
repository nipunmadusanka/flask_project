from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello")

if __name__ == '__main__':
    app.run(debug=True)