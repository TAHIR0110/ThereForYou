from flask import Flask, render_template, request, jsonify
from openai import OpenAI

client = OpenAI(api_key='')

app = Flask(__name__)

# Configure OpenAI API key

# Function to get response from ChatGPT
def send_message(message):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot also a counsellor, you have to console people when the are sad or depressed."},
        {"role": "user", "content": message}
    ],
    max_tokens=100,
    temperature=0.7)
    return response.choices[0].message.content

# Function to convert text to speech using ChatGPT TTS
def convert_to_speech(text):
    # Use the recommended replacement for the deprecated model
    response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text,
)
    response.stream_to_file('output.mp3')
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-transcription', methods=['POST'])
def save_transcription():
    data = request.get_json()
    transcription = data['transcription']
    with open('transcription.txt', 'w') as f:
        f.write(transcription)
    # Get response from ChatGPT
    chat_response = send_message(transcription)
    # Convert response to speech
    convert_to_speech(chat_response)
    return jsonify({'message': 'Transcription saved successfully', 'chat_response': chat_response})

if __name__ == '__main__':
    app.run(debug=True)
