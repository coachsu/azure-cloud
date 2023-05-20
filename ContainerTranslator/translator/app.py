from flask import Flask, request
import requests, uuid

# Azure Translator 金鑰、端點、區域
key = "<your-translator-key>"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "<YOUR-RESOURCE-LOCATION>"

# Azure Translator API
path = '/translate'
constructed_url = endpoint + path

app = Flask(__name__)

@app.route('/')
def hello():
    src = request.args.get('src')
    text = request.args.get('text')
    dst = request.args.get('dst')

    if not src or not text or not dst:
        return "Parameters, src: source language, text: text being translated, dst: destination language are required."
    
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': ['zh-Hant', 'ja']
    }
        
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }
        
    # You can pass more than one object in body.
    body = [{
        'text': 'I would really like to drive your car around the block a few times!'
    }]

    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    result = response.json()
    return f"{result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)