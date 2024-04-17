from flask import Flask, render_template, request, jsonify, send_from_directory
from openai import OpenAI
from pathlib import Path
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import newgender

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    # Get sentiment score
    sentiment_score = analyzer.polarity_scores(text)
    # Return compound score
    return sentiment_score['compound']


client = OpenAI(api_key='')

app = Flask(__name__)

if newgender.essential()=='Male':
    avaj = 'nova'

else :
    avaj = 'echo'


# Function to get response from ChatGPT
def send_message(message):
    # Ensure the message is a string
    if not isinstance(message, str):
        raise ValueError("Message must be a string")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot also a counsellor, you have to console people when they are sad or depressed. also use most human like accent along with umm, uh and sighs so that it could sound more natural"},
            {"role": "user", "content": message}
        ],
        max_tokens=100,
        temperature=0.7
    )

    return response.choices[0].message.content

# def send_message1():
#     # Analyze sentiment
#     data = request.get_json()
#     transcription = data['transcription']
#     with open('transcription.txt', 'w') as f:
#         f.write(transcription)

#     sentiment_score = analyze_sentiment(transcription)
#     # Check if sentiment is negative (below a certain threshold)
#     sadness_flag = sentiment_score < -0.5  # Adjust threshold as needed
#     return sadness_flag


def send_message1(message):
    sentiment_score = analyze_sentiment(message)
    depression_flag = sentiment_score < -0.5
    return depression_flag

def send_message2(message):
    sentiment_score = analyze_sentiment(message)
    sadness_flag = sentiment_score < -0.2
    return sadness_flag
# tts waala function
# import time, taaki nayi url bane har baar audio file ki, while overwriting the same file (storage save krne ke liye)
import time
def convert_to_speech(text):
    speech_file_path =  "static/output.mp3"
    
    response = client.audio.speech.create(
        model="tts-1",
        voice=avaj,
        input=text
    )

    # generated audio save
    response.stream_to_file(speech_file_path)

    # Return the URL to the saved audio with a timestamp as a query parameter
    return f"/output.mp3?{int(time.time())}"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-transcription', methods=['POST'])
def save_transcription():
    data = request.get_json()
    transcription = data['transcription']
    with open('transcription.txt', 'w') as f:
        f.write(transcription)
    # chat gpt ka response
    chat_response = send_message(transcription)
    depressed_detector = send_message1(transcription)
    sad_detector = send_message2(transcription)
    # response to speech aur uska url
    audio_url = convert_to_speech(chat_response)
    return jsonify({'message': 'Transcription saved successfully', 'chat_response': chat_response, 'audio_url': audio_url, 'depressed_flag': depressed_detector, 'sad_detector': sad_detector})



# generated audio file, ki route
@app.route('/output.mp3')
def serve_audio():
    return send_from_directory('static', 'output.mp3')

if __name__ == '__main__':
    app.run(debug=True)
