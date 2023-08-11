from flask import jsonify, request
import requests, json
from flask_jwt_extended import get_jwt_identity

def symptoms(cloud_url):
    patient_id = get_jwt_identity()
    symptoms_list_data = request.json.get('symptomsData')
    json_list_data = json.dumps(symptoms_list_data)
    if(request.method == 'POST'):
        url = f'{cloud_url}/symptoms'
        data = {'identity': patient_id, 'symptoms': json_list_data}
        response = requests.post(url, json=data)
        symptoms_id_list = json.loads(response.json())
        id_list_data = json.dumps(symptoms_id_list)
        return jsonify(id_list_data)

def provider_symptoms(cloud_url, request):
    patient_id = request.json.get('inputValue')
    symptoms_list_data = request.json.get('symptomsData')
    json_list_data = json.dumps(symptoms_list_data)
    if(request.method == 'POST'):
        url = f'{cloud_url}/symptoms'
        data = {'identity': patient_id, 'symptoms': json_list_data}
        response = requests.post(url, json=data)
        symptoms_id_list = json.loads(response.json())
        id_list_data = json.dumps(symptoms_id_list)
        return jsonify(id_list_data)