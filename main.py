from modules.directory_manager import DirectoryManager
from modules.text_extraction.audio_extractor import AudioTextExtractor
from modules.text_extraction.pdf_extractor import PDFTextExtractor
from modules.ppt_integrator import PPTIntegrator
import os

if __name__ == "__main__":
    directory_manager = DirectoryManager()

    # Process audio files
    audio_extractor = AudioTextExtractor(directory_manager)
    for file in os.listdir(directory_manager.get_directory("lectures_audio")):
        if file.endswith((".mp3", ".wav", ".flac")):
            audio_extractor.extract_text(file)

    # Process PDF exams
    pdf_extractor = PDFTextExtractor(directory_manager)
    for file in os.listdir(directory_manager.get_directory("exams")):
        if file.endswith((".pdf", ".docx")):
            pdf_extractor.extract_text(file)

    # Integrate extracted text with PPTs
    ppt_integrator = PPTIntegrator(directory_manager)
    ppt_integrator.integrate_existing_files()

    print("All files processed and cleaned up.")
