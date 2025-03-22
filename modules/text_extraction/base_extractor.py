from abc import ABC, abstractmethod
import os

class TextExtractor(ABC):
    def __init__(self, directory_manager):
        self.directory_manager = directory_manager

    @abstractmethod
    def extract_text(self, file_name: str):
        pass
