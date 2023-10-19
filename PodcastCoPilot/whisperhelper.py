import requests

def whisper_transcribe_audio(prompt: str, file_path: str, endpoint: str, api_version: str, api_key: str):
    # Define headers
    headers = {
        "api-key": api_key
    }

    params = {
        "api-version": api_version
    }

    # Define form data
    with open(file_path, 'rb') as f:
        files = {'file': f}
        form = {
            'language': 'en',
            'prompt': prompt,
            'temperature': '0',
            'response_format': 'json'
        }

        # Make the API request
        response = requests.post(
            endpoint,
            headers=headers,
            params=params,
            files=files,
            data=form
        )
        # Return the response.text as Json
        transcript = response.json()
        return transcript.get('text')
        
#transcript = whisper_transcribe_audio('chunk0.wav', 
#                         "https://weazoairb.openai.azure.com/openai/deployments/whisper/audio/transcriptions",
#                         "2023-09-01-preview",
#                         "f841674ff5654ced9c6930f68803f6ed")
#print(transcript)
