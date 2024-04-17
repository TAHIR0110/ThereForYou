from openai import OpenAI

client = OpenAI(api_key='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')


response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")