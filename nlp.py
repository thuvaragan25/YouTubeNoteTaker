from pytube import YouTube
import os
import json
import whisper
import requests

API_TOKEN = "" #Get your own token from: https://huggingface.co/docs/hub/security-tokens
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(text):
	response = requests.post(API_URL, headers=headers, json=text)
	return response.json()
	

model = whisper.load_model("base")

def extractAudio(link):
    yt = YouTube(link)
    output = yt.streams.filter(only_audio=True).first().download()
    base, _ = os.path.splitext(output)
    filename = base + '.mp3'
    os.rename(output, filename)
    print("Video downloaded!")
    return filename

def transcribeVideo(link, title):
    file_name = extractAudio(link)
    result = model.transcribe(file_name)
    transcribed = result["text"]
    data = { "link" : link, "transcript" : transcribed }
    with open(f"{title}.json", "w") as f:
        json.dump(data, f)
    os.remove(file_name)
    print("Transcribed")
    return transcribed

def summarize(text):
    summarized_text = query({
	    "inputs": text,
    })[0]["summary_text"]
    print("Summarized")
    return summarized_text

