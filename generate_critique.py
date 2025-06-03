import openai
import os
import base64

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_critique(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert art critic analyzing artworks."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe and critique this artwork in detail. Also suggest an existing piece of art that is similar to this."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=500
    )

    return response.choices[0].message.content
