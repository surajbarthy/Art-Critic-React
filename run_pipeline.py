import os
from generate_critique import generate_critique
from generate_audio import text_to_speech
from generate_video import generate_video

def run_pipeline(image_path):
    print("🔵 Generating critique...")
    critique_text = generate_critique(image_path)

    # Generate filenames
    output_name = os.path.basename(image_path).split('.')[0]
    text_file = f"output/{output_name}.txt"
    audio_file = f"audio/{output_name}.mp3"
    video_file = f"videos/{output_name}.mp4"

    print("🟢 Generating speech...")
    text_to_speech(critique_text, output_name)

    print("🟡 Generating video...")
    generate_video(image_path, audio_file, video_file)

    print("✅ Pipeline completed!")
    print(f"📄 Text file: {text_file}")
    print(f"🔊 Audio file: {audio_file}")
    print(f"🎬 Video file: {video_file}")

if __name__ == "__main__":
    image_file = "images/3501.png"  # Change this to your actual image
    run_pipeline(image_file)
