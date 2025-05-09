import requests
import json

def translate(text):
    url = "http://localhost:8097/translate"
    headers = {"Content-Type": "application/json"}
    data = {"text": text}
    # Send a POST request to the translation server
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()["translated_text"]
    else:
        return 'Error: Unable to connect to translation server.'
# function call
if __name__ == "__main__":
    en_text = "你好，今天天氣好"
    translated_text = translate(en_text)
    print(f"Translated text: {translated_text}")