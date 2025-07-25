''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """ Process the text to analyze """
     # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # If 404 status code
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!\n"

    # Format the output text
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}.\n"
    )
    # Print output for screenshot
    print(output)
    # Return a formatted string in the formatted output
    return output

@app.route("/")
def render_index_page():
    """ Html page to submit request for analysis """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
