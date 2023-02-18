from nlp import transcribeVideo, summarize
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        transcript = ""
        data = request.form
        link = data['link']
        title = data['title']
        transcript = transcribeVideo(link, title)
        summary = summarize(transcript)
        return render_template('index.html', transcript=transcript, summary=summary)

if __name__ == "__main__":
    app.run('0.0.0.0', 3000, debug=True)