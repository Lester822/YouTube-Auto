import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin

URL = "http://127.0.0.1:7860"


def generate_image(prompt, path, *, width=1280, height=720, steps=42, negative_prompt='text'):
    payload = {
        "prompt": prompt,
        "steps": steps,
        "width": width,
        "height": height,
        "negative_prompt": negative_prompt
    }
    response = requests.post(url=f'{URL}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{URL}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(path, pnginfo=pnginfo)