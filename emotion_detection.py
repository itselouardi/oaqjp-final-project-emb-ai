import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=input_json, headers=header)
    if res.status_code == 200:
        return res.json()
    else:
        return {"error": f"Request failed with status code {res.status_code}"}


if __name__ == "__main__":
    sample_text = "I am very happy today!"
    result = emotion_detector(sample_text)
    print(result)