import os
import subprocess

def generate_video(image_path, audio_path, output_path, duration=30):
    """
    Uses FFmpeg to generate a video using the provided image and audio.
    
    :param image_path: Path to the input image.
    :param audio_path: Path to the input audio file.
    :param output_path: Path to the output video file.
    :param duration: Duration of the video in seconds (default: 30).
    """

    # Check if files exist
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    # FFmpeg command to create video
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",  # Overwrite output file if exists
        "-loop", "1",  # Loop image for video
        "-i", image_path,  # Input image
        "-i", audio_path,  # Input audio
        "-c:v", "libx264",  # Encode video in H.264
        "-tune", "stillimage",  # Optimize for a still image
        "-c:a", "aac",  # Audio codec
        "-b:a", "192k",  # Audio bitrate
        "-pix_fmt", "yuv420p",  # Ensures compatibility with most players
        "-shortest",  # Ensures video is cut to the length of the shortest input
        output_path  # Output file
    ]

    # Run FFmpeg command
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"🎬 Video generated: {output_path}")

if __name__ == "__main__":
    image_file = "images/3506.png"  # Your render image
    audio_file = "audio/3506.mp3"  # Generated critique audio
    output_video = "videos/3506.mp4"  # Output video file

    # Ensure output folder exists
    os.makedirs("videos", exist_ok=True)

    # Generate video
    generate_video(image_file, audio_file, output_video)
