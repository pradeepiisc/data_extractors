import os

class DataExtractor:
    def __init__(self, source_format, target_format):
        self.source_format = source_format
        self.target_format = target_format

    def extension_check(self, file_path):
        file_name, file_extension = self._get_file_name_extension(file_path)
        print("File Name - ", file_name)
        if self.source_format not in file_extension:
            print("{} not a {}".format(file_path, self.source_format))
            return False
        return True
    
    def get_output_file_path(self, source_path, destination_dir):
        file_name, file_extension = self._get_file_name_extension(source_path)
        return os.path.join(destination_dir, file_name + "."+ self.target_format)
    
    def get_file_records(self, source_file_path):
        raise NotImplementedError("Subclasses must implement convert_file method.")

    def convert_file(self, source_file_path, destination_file_path):
        """
        Source file path is an absolute path with the file name in the end
        destination_file_path is an absolute path(WITHOUT file name in the end) where text file is to be saved 
        """
        raise NotImplementedError("Subclasses must implement convert_file method.")
    


    def convert_directory(self, source_dir, destination_dir):
        """
        Source Directory is the directory with subdirectories and files to be converted to text
        Destination directory is the location where to store the converted files in same structure

        Make sure the destination location is not the same as the source_directory parent location
        """
        for root, dirs, files in os.walk(source_dir):
            # print("Inside for loop")
            # Create the corresponding directory structure in the destination directory
            for directory in dirs:
                source_path = os.path.join(root, directory)
                # print(source_path)
                relative_path = os.path.relpath(source_path, source_dir)
                # print(relative_path)
                destination_path = os.path.join(destination_dir, relative_path)
                # print(destination_path)
                os.makedirs(destination_path, exist_ok=True)

            # print("Total files to process are {}".format(len(files)))
            # Process the files to the destination directory
            for file in files:
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                destination_path = os.path.join(destination_dir, relative_path, "") # file.split("pdf")[0]+"txt"
                # print(destination_path)
                self.convert_file(source_file_path=source_file, destination_file_path=destination_path)
        return
    
    def convert(self,  source_file_path, destination_file_path):
        if not os.path.isdir(destination_file_path):
            print("Destination path should be a directory not a file")
            print("Please pass a correct destination directory location")
            return
        if os.path.isfile(source_file_path):
            print("Found file in source path - converting the file")
            self.convert_file(source_file_path, destination_file_path)
        elif os.path.isdir(source_file_path):
            print("Found directory in the source path - converting files recuresively")
            self.convert_directory(source_file_path, destination_file_path)
        else:
            print("Invalid path:", source_file_path)
    
    def _get_file_name_extension(self, file_path):
        fname, fextension = os.path.splitext(os.path.basename(file_path))
        return fname, fextension.lstrip(".")
