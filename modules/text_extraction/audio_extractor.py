import os
from .base_extractor import TextExtractor

class AudioTextExtractor(TextExtractor):
    def transcribe_audio_api(self, audio_path):
        return f"Transcribed text for {os.path.basename(audio_path)}"

    def extract_text(self, file_name: str = None):
        audio_dir = self.directory_manager.get_directory("lectures_audio")
        extracted_text_dir = self.directory_manager.get_directory("extracted_text")

        audio_files = [f for f in os.listdir(audio_dir) if f.endswith((".mp3", ".wav", ".flac"))]

        if file_name:  # Process only a specific file
            audio_files = [file_name] if file_name in audio_files else []

        for audio_file in audio_files:
            audio_path = os.path.join(audio_dir, audio_file)
            transcribed_text = self.transcribe_audio_api(audio_path)

            text_filename = os.path.splitext(audio_file)[0] + ".txt"
            text_path = os.path.join(extracted_text_dir, text_filename)

            with open(text_path, "w") as text_file:
                text_file.write(transcribed_text)
            print(f"Extracted text saved as {text_path}")

           
