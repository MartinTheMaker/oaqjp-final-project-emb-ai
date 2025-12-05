"""
Flask web server for the Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the main HTML interface for the application.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detection_endpoint():
    """
    Flask endpoint that receives a text statement, calls the emotion_detector
    function from the EmotionDetection package, and returns a formatted response.

    Returns
    -------
    str
        A formatted text string describing the emotion scores and dominant emotion,
        or an error message if the input is invalid.
    """
    statement = request.args.get("statement")

    result = emotion_detector(statement)

    # If the detection returned None values → invalid input
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
