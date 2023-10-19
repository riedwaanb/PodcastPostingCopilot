from promptflow import tool
from promptflow.connections import CustomConnection
import requests

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(guestname: str, conn: CustomConnection) -> str:
  print("Search term is " + guestname)

  headers = {"Ocp-Apim-Subscription-Key": conn.secrets['key']}
  params = {"q": guestname, "textDecorations": True, "textFormat": "HTML"}
  response = requests.get(conn.configs['endpoint'], headers=headers, params=params)
  response.raise_for_status()
  search_results = response.json()

  # Parse out a bio.  
  bio = search_results["webPages"]["value"][0]["snippet"]
  
  return bio
