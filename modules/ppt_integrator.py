import os

class PPTIntegrator:
    def __init__(self, directory_manager):
        self.directory_manager = directory_manager

    def integrate_existing_files(self):
        ppt_dir = self.directory_manager.get_directory("ppts")
        extracted_text_dir = self.directory_manager.get_directory("extracted_text")
        result_dir = self.directory_manager.get_directory("results")

        ppt_files = [os.path.join(ppt_dir, f) for f in os.listdir(ppt_dir) if f.endswith((".ppt", ".pptx"))]
        text_files = [os.path.join(extracted_text_dir, f) for f in os.listdir(extracted_text_dir) if f.endswith(".txt")]

        for ppt_file in ppt_files:
            self.send_to_api(ppt_file, text_files, result_dir)


    def send_to_api(self, ppt_path, text_files, result_dir):
        print(f"Sending PPT and extracted text files to API for {ppt_path}...")
        
        # Mock API processing
        print("API processing complete. Saving result...")

        # Generate result file path
        result_file_path = os.path.join(result_dir, os.path.basename(ppt_path))

        with open(result_file_path, "w") as result_file:
            result_file.write("Mock processed PPT result")

        print(f"Processed PPT saved in {result_file_path}")
