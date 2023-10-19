from promptflow import tool
from promptflow.connections import CustomConnection

from pydub import AudioSegment
from pydub.silence import split_on_silence
from whisperhelper import whisper_transcribe_audio
import requests

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(url: str, prompt: str, conn: CustomConnection) -> str:
  # Download the file from `url` and save it locally under `file_name`:
  file_name = "podcast.mp3"
  response = requests.get(url)
  with open(file_name, "wb") as f:
    f.write(response.content)

  # Chunk up the audio file 
  sound_file = AudioSegment.from_mp3(file_name)
  audio_chunks = split_on_silence(sound_file, min_silence_len=1000, silence_thresh=-40 )
  count = len(audio_chunks)
  print("Audio split into " + str(count) + " audio chunks")
  transcript = ""

  # Call Whisper to transcribe audio
  for i, chunk in enumerate(audio_chunks):
      # If you have a long audio file, you can enable this to only run for a subset of chunks
      if i < 10 or i > count - 10:
          out_file = "chunk{0}.wav".format(i)
          chunk.export(out_file, format="wav")

          # Call Whisper to transcribe audio
          transcriptChunk = whisper_transcribe_audio(prompt, out_file, conn.configs['endpoint'], conn.configs['version'], conn.secrets['key'])
          
          # Append transcript in memory
          transcript += " " + transcriptChunk

  return transcript
