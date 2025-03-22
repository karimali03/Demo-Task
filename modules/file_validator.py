import os

class FileValidator:
    allowed_extensions = {
        "exams": [".pdf", ".docx"],
        "lectures_audio": [".mp3", ".wav", ".flac"],
        "ppts": [".ppt", ".pptx"]
    }

    @staticmethod
    def is_valid(file_path: str, file_type: str):
        file_extension = os.path.splitext(file_path)[1].lower()
        return file_extension in FileValidator.allowed_extensions.get(file_type, [])
