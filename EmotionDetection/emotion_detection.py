import requests, json

def emotion_detector(text_to_analyze):
    # Check for blank entry
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json=input_json, headers=header)
    
    # Handle status code 400 (blank entry)
    if res.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Handle other error status codes
    if res.status_code != 200:
        return {"error": f"Request failed with status code {res.status_code}"}
    
    output = json.loads(res.text)
    emotions = output['emotionPredictions'][0]['emotion']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)
    return emotions


if __name__ == "__main__":
    # Test with blank entry
    print("Testing with blank entry:")
    blank_result = emotion_detector("")
    print(blank_result)
    
    print("\nTesting with valid text:")
    sample_text = "I love this new technology."
    result = emotion_detector(sample_text)
    print(result)