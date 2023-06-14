from data_extractor import DataExtractor

# Example implementation of HTML to XML converter
class HtmlToXmlConverter(DataExtractor):
    def __init__(self):
        super().__init__('html', 'xml')
    
    def get_file_records(self, source_file_path):
        success = self.extension_check(file_path=source_file_path)
        if not success:
            return []
        print("processing File at {}".format(source_file_path ))

        records = []
        return records
    
    def convert_file(self, source_file_path, destination_file_path):
        pass