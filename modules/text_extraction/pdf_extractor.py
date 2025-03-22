import os
from .base_extractor import TextExtractor

class PDFTextExtractor(TextExtractor):
    def extract_text(self, file_name: str = None):
        exams_dir = self.directory_manager.get_directory("exams")
        extracted_text_dir = self.directory_manager.get_directory("extracted_text")

        pdf_files = [f for f in os.listdir(exams_dir) if f.endswith((".pdf", ".docx"))]

        if file_name:  # Process only a specific file
            pdf_files = [file_name] if file_name in pdf_files else []

        for pdf_file in pdf_files:
            pdf_path = os.path.join(exams_dir, pdf_file)
            extracted_text = self.mock_extract_text(pdf_path)

            text_filename = os.path.splitext(pdf_file)[0] + ".txt"
            text_path = os.path.join(extracted_text_dir, text_filename)

            with open(text_path, "w") as text_file:
                text_file.write(extracted_text)
            print(f"Extracted text saved as {text_path}")

      
    def mock_extract_text(self, pdf_path):
        return f"Mock extracted text from {os.path.basename(pdf_path)}"
