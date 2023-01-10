from pytube import YouTube
import os
import json
import whisper

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
    return transcribed