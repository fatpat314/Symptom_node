import config
from dotenv import load_dotenv
from flask import Flask, jsonify, request, session, g
from flask_jwt_extended import JWTManager, jwt_required
from flask_cors import CORS

import argparse, requests, json

from symptoms_form import symptoms, provider_symptoms

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY # change this to a random string in production
cloud_url = "http://localhost:8010"
# cloud_url = "https://cognitive-network-manager-rdwl5upzra-uw.a.run.app"
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
        data = "Symptoms Node"
        return jsonify({'data': data})

@app.route('/symptoms', methods = ['POST'])
@jwt_required()
def symptoms_form():
    return symptoms(cloud_url)

@app.route('/care_provider_symptoms', methods=['POST'])
@jwt_required()
def care_provider_symptoms_form():
    try:
        id_list_data = provider_symptoms(cloud_url, request)
    except:
        return
    patient_id = request.json.get('inputValue')
    symptoms_id = id_list_data
    event_url = get_event_server()
    event_url = event_url['url']
    event_url = f'{event_url}/event-patient-symptoms'
    print("ID", symptoms_id)
    data = {'patient_id': patient_id, 'symptoms_id': symptoms_id}
    event_response = requests.post(event_url, json=data)
    id_list_data = json.dumps(id_list_data)
    return jsonify(id_list_data)
    # return(id_list_data)

def get_event_server():
    event_url = f'{cloud_url}/event_server'
    response = requests.get(event_url)
    return response.json()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8080, help="Port to run the server on")
    args = parser.parse_args()
    port = args.port
    app.run(host="0.0.0.0", port=port)