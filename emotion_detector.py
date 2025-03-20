import requests
import json

def emotion_predictor(text):
    """
    Function to predict the emotion of a given text using Watson NLP API.
    """
    api_url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/v1/analyze"
    api_key = "your_ibm_watson_api_key"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "features": {"emotion": {}}
    }

    response = requests.post(api_url, headers=headers, json=payload, auth=("apikey", api_key))

    if response.status_code == 200:
        emotions = response.json()['emotion']['document']['emotion']
        return emotions
    else:
        return {"error": "Could not analyze emotions"}

# Example usage
if __name__ == "__main__":
    text_input = "I am extremely happy today!"
    print(emotion_predictor(text_input))
