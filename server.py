'''Import Flask, render_template, request from the flask framework package '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    ''' Retrieve the Provided text to analyze from the request arguments'''
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract anger,disgust,fear,joy,sadness,dominant_emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Check if the label is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    # Return a formatted string with the sentiment label and score
    response_str=f"""For the given statement, the system response is
    'anger' : {anger}, 'disgust' : {disgust},'fear' : {fear}, 'joy' : {joy} and 'sadness' : {sadness}. 
    The dominant emotion is {dominant_emotion}."""
    return response_str

@app.route("/")
def render_index_page():
    '''Render the index page to the user, this is where the text string to be
    analyzed is provided and a response is displayed back to the user.
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
