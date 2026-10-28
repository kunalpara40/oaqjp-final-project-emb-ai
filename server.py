
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def render_index_page():
    return render_template('index.html')


@app.route('/emotionDetector')
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze', '')

    if not text_to_analyze.strip():
        return "Invalid text! Please enter a statement to analyze.", 400

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Unable to analyze the given text. Please try again.", 500

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Unable to determine the dominant emotion. Please try again.", 500

    return (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} "
        "and 'sadness': {}. The dominant emotion is {}."
    ).format(
        anger, disgust, fear, joy, sadness, dominant_emotion
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
