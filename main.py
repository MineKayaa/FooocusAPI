from fastapi import FastAPI, File, UploadFile
import replicate
from dotenv import load_dotenv
load_dotenv()

import base64

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/model")
async def get_response(prompt: str, img1: UploadFile, img2: UploadFile):

    cn_img1 = ProcessFile(img1)
    cn_img2 = ProcessFile(img2)

    input={
        "prompt": prompt,
        "cn_img1": cn_img1,
        "cn_img2": cn_img2,
        "cn_type1": "ImagePrompt",
        "cn_type2": "ImagePrompt",
        "cn_type3": "ImagePrompt",
        "cn_type4": "ImagePrompt",
        "sharpness": 2,
        "image_seed": 50403806253646856,
        "uov_method": "Disabled",
        "image_number": 1,
        "guidance_scale": 4,
        "refiner_switch": 0.5,
        "negative_prompt": "",
        "style_selections": "Fooocus V2,Fooocus Enhance,Fooocus Sharp",
        "uov_upscale_value": 0,
        "outpaint_selections": "",
        "outpaint_distance_top": 0,
        "performance_selection": "Speed",
        "outpaint_distance_left": 0,
        "aspect_ratios_selection": "1152*896",
        "outpaint_distance_right": 0,
        "outpaint_distance_bottom": 0,
        "inpaint_additional_prompt": ""
    }
    output = replicate.run(
        "konieshadow/fooocus-api:fda927242b1db6affa1ece4f54c37f19b964666bf23b0d06ae2439067cd344a4",
        input=input
    )
    return output


def ProcessFile(img):
    print(img)
    contents = img.file.read()
    data = base64.b64encode(contents).decode('utf-8')
    cn_img1 = f"data:application/octet-stream;base64,{data}"
    return cn_img1

