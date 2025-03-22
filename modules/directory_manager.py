import os

class DirectoryManager:
    def __init__(self, base_dir="assets"):
        self.base_dir = base_dir
        self.directories = {
            "exams": os.path.join(base_dir, "exams"),
            "lectures_audio": os.path.join(base_dir, "lectures_audio"),
            "ppts": os.path.join(base_dir, "ppts"),
            "extracted_text": "./extracted_text",
            "results": "./results"
        }
        self._create_directories()

    def _create_directories(self):
        for directory in self.directories.values():
            os.makedirs(directory, exist_ok=True)

    def get_directory(self, file_type: str):
        return self.directories.get(file_type, None)

    def get_available_types(self):
        return list(self.directories.keys())
