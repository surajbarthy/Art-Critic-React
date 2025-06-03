import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_to_speech(text, output_filename):
    response = openai.audio.speech.create(
        model="tts-1",  # OpenAI’s text-to-speech model
        voice="shimmer",  # Other voices: alloy, echo, fable, nova, shimmer, onyx
        input=text
    )

    # Save audio file
    audio_path = f"audio/{output_filename}.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)

    print(f"Generated audio saved to {audio_path}")
    return audio_path  # Returning the audio file path

if __name__ == "__main__":
    sample_text = "This is a test audio for the art critique."
    text_to_speech(sample_text, "test_audio")
