import os
import requests
import uuid
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.environ['KEY']
location = os.environ['LOCATION']


def get_translation(text_input, language_output):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=' + language_output
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text_input}]

    response = requests.post(constructed_url, headers=headers, json=body)
    return response.json()
