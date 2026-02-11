import os
import whisper

input_dir = "videos"
output_dir = "transcripts"

os.makedirs(output_dir, exist_ok=True)

# possible models: tiny, base, small, medium, large
model = whisper.load_model("large")

video_exts = {".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"}

for root, _, files in os.walk(input_dir):
    for f in files:
        if os.path.splitext(f)[1].lower() in video_exts:
            video_path = os.path.join(root, f)
            base_name = os.path.splitext(f)[0]
            txt_path = os.path.join(output_dir, f"{base_name}.txt")

            print(f"🎙️ Transcribing: {video_path} ...")

            # Transcribe video in Romanian with diacritics (ă, â, î, ș, ț)
            result = model.transcribe(
                video_path,
                language="ro",
                initial_prompt="Aceasta este o transcriere în limba română cu diacritice corecte: ă, â, î, ș, ț, Ă, Â, Î, Ș, Ț.",
            )

            # Transcribe video in English
            # result = model.transcribe(video_path, language="en")

            with open(txt_path, "w", encoding="utf-8") as out:
                out.write(result["text"])

print("DONE")