from data_extractor import DataExtractor

class XmlToTextConverter(DataExtractor):
    def __init__(self):
        super().__init__('xml', 'txt')

    def get_file_records(self, source_file_path):
        success = self.extension_check(file_path=source_file_path)
        if not success:
            return []
        print("processing File at {}".format(source_file_path ))

        records = []
        return records
    
    def convert_file(self, source_file_path, destination_file_path):
        records = self.get_file_records(source_file_path=source_file_path)
        # Write recors to destination path
        pass
