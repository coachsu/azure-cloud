import logging
import requests, uuid
import azure.functions as func

# Azure Translator 金鑰、端點、區域
key = "<your-translator-key>"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "<YOUR-RESOURCE-LOCATION>"

# Azure Translator API
path = '/translate'
constructed_url = endpoint + path

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    src = req.params.get('src')
    text = req.params.get('text')
    dst = req.params.get('dst')

    if not src or not text or not dst:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            src = req_body.get('src')
            text = req_body.get('text')
            dst = req_body.get('dst')

    if src and text and dst:
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

        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        return func.HttpResponse(f"{response}")
    else:
        return func.HttpResponse(
            "Parameters, src: source language, text: text being translated, dst: destination language are required.",
            status_code=200
        )