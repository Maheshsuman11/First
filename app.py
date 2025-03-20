from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime
from gtts import gTTS

app = Flask(__name__)

# Ensure the audio directory exists
os.makedirs("static/audio", exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-voice', methods=['POST'])
def generate_voice():
    data = request.json
    text = data.get('text')

    # Generate audio using gTTS
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    audio_filename = f"output_{timestamp}.mp3"
    audio_path = os.path.join("static", "audio", audio_filename)
    tts = gTTS(text=text, lang='hi')
    tts.save(audio_path)

    audio_url = f"/static/audio/{audio_filename}"
    return jsonify({'audio_url': audio_url})

if __name__ == '__main__':
    app.run(debug=True)