import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise if necessary
    r.adjust_for_ambient_noise(source)

    # Continuously listen for speech
    while True:
        try:
            # Capture the audio data
            audio = r.listen(source)

            # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio)

            # Print the transcribed speech
            print("You said:", text)

        # Handle errors
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
