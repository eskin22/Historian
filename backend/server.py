from flask import Flask, request, send_from_directory
from flask_cors import CORS, cross_origin
from flask import jsonify
import json
import os

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api', methods=['GET'])
def get_data():
    return {'message': '✅'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)