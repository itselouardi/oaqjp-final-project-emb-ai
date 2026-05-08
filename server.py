'''
Executing this script initiates the application of emotion
detection to be executed over the Flask and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    '''
    Receives the text from the index.html and
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the emotions and their
    scores.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and "
    f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    '''
    Render the main application page over the Flask.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)