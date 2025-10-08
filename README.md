# AI Video Transcript

A simple Python project that transcribes videos into text using [OpenAI Whisper](https://github.com/openai/whisper).

## 📂 Project structure

```
ai-video-transcript/
│
├── app.py            # main script for transcription
├── transcripts/      # generated text transcripts
├── videos/           # input video files
├── .gitignore
└── README.md
```

---

## 🧠 Instructions

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt --break-system-packages
brew install ffmpeg

# 3. Add your video file
# Place your video in the "videos" folder (e.g., videos/all-info.MOV)

# 4. Run transcription
python3 app.py

# 5. Check output
# The transcript will be saved in the "transcripts" folder as a .txt file
```

---

## 📦 requirements.txt

```txt
openai-whisper
```

*(Optional — you can generate this automatically with `pip freeze > requirements.txt`)*

---

## 🔧 Features

Whisper can be used for more than just video-to-text transcription:

* Transcription → Convert audio files (mp3, wav, m4a, etc.) into text.
* Translation → Translate non-English speech directly into English text.
* Subtitles → Generate `.srt` or `.vtt` subtitle files from videos.
* Voice Notes → Turn recorded voice memos into searchable text.
* Meetings & Lectures → Automatically transcribe recordings.
* Multilingual Audio → Recognize and transcribe speech in many languages.

---

## 🌐 More AI Projects

* [Coqui TTS](https://github.com/coqui-ai/TTS) → Text-to-speech for natural voices.
* [Riffusion](https://github.com/riffusion/riffusion-hobby) → Real-time music generation with diffusion models.
* [Stable Diffusion](https://github.com/CompVis/stable-diffusion) → High-quality image generation with text prompts.