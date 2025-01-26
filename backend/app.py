import boto3
import json
from flask import Flask, request, jsonify
from botocore.exceptions import ClientError

app = Flask(__name__)

def get_secret_value(secret_name):
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name="ap-south-1")
    try:
        response = client.get_secret_value(SecretId=secret_name)
        if "SecretString" in response:
            secret = response["SecretString"]
            secret_dict = json.loads(secret)
            return secret_dict["API_KEY"]
        else:
            return None
    except ClientError as e:
        print(f"Error retrieving secret: {e}")
        return None

API_KEY = get_secret_value("my-api-key-secret")

if API_KEY is None:
    raise ValueError("API_KEY could not be retrieved from AWS Secrets Manager")

def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/number-info', methods=['GET'])
def number_info():
    api_key = request.headers.get('X-API-Key')
    if api_key != API_KEY:
        return jsonify({"message": "Unauthorized access. Invalid or missing API key."}), 403

    number = request.args.get('number', type=int)
    
    if number is None:
        return jsonify({"message": "Bad request. Please provide a number."}), 400

    result = {
        "number": number,
        "is_even": number % 2 == 0,
        "is_odd": number % 2 != 0,
        "is_prime": check_prime(number)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
