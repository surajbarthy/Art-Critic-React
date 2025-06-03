import openai
import os
import base64

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_critique(image_path):
    # Convert image to Base64
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    # API call to analyze image and generate critique
    response = openai.chat.completions.create(
        model="gpt-4o",  # Ensure you have access to GPT-4o with Vision
        messages=[
            {"role": "system", "content": "You are an expert art critic analyzing artworks."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe and critique this artwork in detail.  Also suggest an existing piece of art that is similar to this based on your analysis. Check and make sure that it is an existing artwork."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=500
    )

    critique_text = response.choices[0].message.content

    # Save critique to a text file
    critique_filename = f"output/{os.path.basename(image_path).split('.')[0]}.txt"
    with open(critique_filename, "w") as f:
        f.write(critique_text)

    print(f"Generated critique saved to {critique_filename}")
    return critique_text  # Returning text for audio generation

if __name__ == "__main__":
    image_file = "images/3506.png"  # Ensure the file exists in the /images folder
    generate_critique(image_file)
