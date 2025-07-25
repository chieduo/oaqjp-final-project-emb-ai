import requests
import json

def emotion_detector(text_to_analyse):
    """ analyze text to respond with the user's emotional state """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Text to analyze
    payload = { "raw_document": { "text": text_to_analyse } }
    # Header for the text to analyze
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    # making the api request
    response = requests.post(url, json=payload, headers=headers)
    # if response is not a successful one, throw exception
    if response.status_code != 200:
        print("API Error:", response.status_code, response.text)
        raise Exception("Emotion prediction failed")
    # return text after successful reponse
    return response.text
