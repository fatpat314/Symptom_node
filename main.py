import config
from dotenv import load_dotenv
from flask import Flask, jsonify, request, session, g
from flask_jwt_extended import JWTManager, jwt_required
# import requests, json
import argparse

from symptoms_form import symptoms, provider_symptoms

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY # change this to a random string in production
cloud_url = "http://localhost:6000"
jwt = JWTManager(app)
load_dotenv()

class Symptom:
    # What makes a symptom?
    # Name
    # Log of who and when
    pass

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        data = "hello Class!"
        return jsonify({'data': data})

@app.route('/symptoms', methods = ['POST'])
@jwt_required()
def symptoms_form():
    return symptoms(cloud_url)

@app.route('/care_provider_symptoms', methods=['POST'])
@jwt_required()
def care_provider_symptoms_form():
    return provider_symptoms(cloud_url, request)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080, help="Port to run the server on")
    args = parser.parse_args()
    port = args.port
    app.run(host="0.0.0.0", port=port)