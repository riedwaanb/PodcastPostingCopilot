# PodcastPostingCopilot
This code was used to demonstrate the power of PromptFlow for building Copilots at the Era of AI event in 2024 in Johannesburg, South Africa.
This is not an official Microsoft Project. It is a personal demonstration.

# Inspiration
I've taken inspiration from Build 2023 keynote by Microsoft CTO Kevin Scott. [here](https://github.com/microsoft/PodcastCopilot)

# Flow
This podcast posting Copilot makes it easier to generate a social media post given a url link to a podcast. Using PromptFlow, to orchestrate a series of code, AI models, data and LLM prompts.
The following is what has been orchestrated by PromptFlow:
+ Given a Audio Podcast URL, its downloaded locally and using the Azure OpenAI Whisper Model, a transciption is generated
+ With the Transcription, the Guest name is retrieved using an Azure OpenAI GPT3.5 model
+ With the Guest name, their Bio is retrieved using the Bing Search API
+ With the Transcription and Guest Bio, a summarised social media copy is generated using Azure OpenAI GPT3.5 model
+ With the Social Media copy, a relevant prompt for DALL-E is created using using Azure OpenAI GPT4 model
+ With the DALL-E prompt, the DALL-E model generated a corresponding image for the post.
+ Finally, a comprehensive LinkedIn social media post is generated from the Social Media Copy, Podcast URL and DALL-E image

## Setup
This project requires creating an Azure OpenAI resource to run several cloud-based models.  
+ You can request access to Azure OpenAI at https://aka.ms/oai/access.  
+ After approval, create an Azure OpenAI resource at https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI following the instructions at https://learn.microsoft.com/azure/cognitive-services/openai/how-to/create-resource.  
+ You will need to create model deployments of the following models: gpt-4, dalle, and a plugins-capable model.  Follow the instructions [here](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource#deploy-a-model).
+ Some models such as GPT4 and Whisper at time of writing are only available is certain Azure Regions.
+ You will need to create a Bing search resource [here](https://portal.azure.com/#create/Microsoft.BingSearch)
+ You will need PromptFlow from the vscode marketplace [here](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

Set up your environment using the following commands:
```
pip install -r requirements.txt
```
