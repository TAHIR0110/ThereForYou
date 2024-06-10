from flask import Flask, jsonify, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Configure OpenAI API key
client = OpenAI(api_key="")


# Function to get response from ChatGPT
def send_message(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a chatbot also a counsellor, you have to console people when the are sad or depressed.",
            },
            {"role": "user", "content": message},
        ],
        max_tokens=100,
        temperature=0.7,
    )
    return response.choices[0].message.content


from pathlib import Path


# Function to convert text to speech using ChatGPT TTS
def convert_to_speech(text):
    # Specify the file path to save the speech
    speech_file_path = Path(__file__).parent / "static/output.mp3"

    # Generate spoken audio from input text
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=text)

    # Save the generated audio to the specified file path
    response.stream_to_file(speech_file_path)

    # Return the file path to the saved audio
    return str(speech_file_path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save-transcription", methods=["POST"])
def save_transcription():
    data = request.get_json()
    transcription = data["transcription"]
    with open("transcription.txt", "w") as f:
        f.write(transcription)
    # Get response from ChatGPT
    chat_response = send_message(transcription)
    # Convert response to speech and get the URL
    audio_url = convert_to_speech(chat_response)
    return jsonify(
        {
            "message": "Transcription saved successfully",
            "chat_response": chat_response,
            "audio_url": audio_url,
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
