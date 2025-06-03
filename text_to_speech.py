import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_to_speech(text_file):
    with open(text_file, "r") as f:
        critique_text = f.read()

    response = openai.audio.speech.create(
        model="tts-1",
        voice="coral",
        input=critique_text
    )

    audio_filename = f"audio/{os.path.basename(text_file).split('.')[0]}.mp3"
    with open(audio_filename, "wb") as f:
        f.write(response.content)

    print(f"Generated audio saved to {audio_filename}")
    return audio_filename

# Example usage
if __name__ == "__main__":
    text_file = "output/zoe.txt"  # Change this for other files
    text_to_speech(text_file)
