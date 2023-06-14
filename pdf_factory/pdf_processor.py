# from collections import defaultdict
# record_dict = defaultdict(list)
# record_dict["text"]     # Accessing the "text" key will return an empty list []
# record_dict["image"] # Accessing the "image" key will return an empty list []

class Record:
    def __init__(self, text, image):
        self.text = text
        self.image = image

class DataContainer:
    def __init__(self):
        self.records = []
        
    def add_record(self, text, image):
        record = Record(text, image)
        self.records.append(record)
        
    def get_records(self):
        return self.records


class FileProcessor:
    def __init__(self):
        self.data = DataContainer()

    def process_file(self, file_path):
        raise NotImplementedError("Subclass should implement this function")


class PdfProcessor(FileProcessor):
    def __init__(self) -> None:
        super().__init__()
        pass

class HtmlProcessor(FileProcessor):
    def __init__(self) -> None:
        super().__init__()
        pass
        
class XmlProcessor(FileProcessor):
    def __init__(self) -> None:
        super().__init__()
        pass