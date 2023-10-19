from promptflow import tool
from promptflow.connections import CustomConnection
import requests
import openai

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(dalle_prompt: str, conn: CustomConnection) -> str:
  openai.api_key = conn.secrets['key']
  
  response = openai.Image.create(prompt=dalle_prompt, n=1, size = "512x512")
  imageURL = response["data"][0]["url"]
  print("Image URL: " + imageURL + "\n")

  # Write imageURL to file
  photo_path = ".\PostImage.png"
  with open(photo_path, "wb") as f:
    response = requests.get(imageURL)
    f.write(response.content)
  
  return imageURL

