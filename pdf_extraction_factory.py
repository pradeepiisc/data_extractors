from data_extractor import DataExtractor
from pdf_factory.pdf_miner import PdfMinerParser
from pdf_factory.py_mu_pdf import PyMuPdfParser

class PDFMinerConverter(DataExtractor):
    def __init__(self):
        self.pdf_miner_parser = PdfMinerParser()
        super().__init__('pdf', 'txt')

    def get_file_records(self, source_file_path):
        success = self.extension_check(file_path=source_file_path)
        if not success:
            return []
        print("processing File at {}".format(source_file_path ))

        records = self.pdf_miner_parser.process_file(source_file_path)
        return records
        
        
    
    def convert_file(self, source_file_path, destination_file_path):
        print("Inside pdfminerconverter convert_file function")
        records = self.get_file_records(source_file_path=source_file_path)
        if records is None or len(records) <= 0:
            print("No records found")
            return

        print("Total records found {}".format(len(records)))
        # print(records[0].text)
        # print(records[0].image)

        output_file_path = self.get_output_file_path(source_path=source_file_path,
                                                    destination_dir=destination_file_path)
        print("Output file path - ", output_file_path)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            for line in records:
                print(line.text,file=f)
        
        print("Converted using PDFMiner")
        return


class PyMuPDFConverter(DataExtractor):
    def __init__(self):
        self.pdf_parser = PyMuPdfParser()
        super().__init__('pdf', 'txt')

    def get_file_records(self, source_file_path):
        success = self.extension_check(file_path=source_file_path)
        if not success:
            return []
        print("processing File at {}".format(source_file_path ))

        records = self.pdf_parser.process_file(source_file_path)
        return records
    
    def convert_file(self, source_file_path, destination_file_path):
        print("Inside pdfminerconverter convert_file function")
        records = self.get_file_records(source_file_path=source_file_path)
        if records is None or len(records) <= 0:
            print("No records found")
            return

        print("Total records found {}".format(len(records)))
        output_file_path = self.get_output_file_path(source_path=source_file_path,
                                                    destination_dir=destination_file_path)
        print("Output file path - ", output_file_path)
        # Store the result in output_file_path
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for line in records:
                print(line.text,file=f)
        print("Converted using PyMuPDF")
        return


class PdfConverterFactory(DataExtractor):
    def __init__(self, library):
        self.library = library
        self.pdf_parser = self.create_converter(library)
        super().__init__('pdf', 'txt')
        return

    def get_file_records(self, source_file_path):
        print("Getting File records using {} library".format(self.library))
        success = self.extension_check(file_path=source_file_path)
        if not success:
            return []
        print("processing File at {}".format(source_file_path ))

        records = self.pdf_parser.process_file(source_file_path)
        return records
    
    def convert_file(self, source_file_path, destination_file_path):
        print("Inside {} convert_file function".format(self.library))
        print("Converting file {} ".format(source_file_path))
        records = self.get_file_records(source_file_path=source_file_path)
        if records is None or len(records) <= 0:
            print("No records found")
            return

        print("Total records found {}".format(len(records)))

        # print(records[0].text)
        # print(records[0].image)

        output_file_path = self.get_output_file_path(source_path=source_file_path,
                                                    destination_dir=destination_file_path)
        print("Output file path - ", output_file_path)
        # Store the result in output_file_path
        with open(output_file_path, 'w', encoding='utf-8') as f:
            for line in records:
                print(line.text,file=f)
        print("Converted using {}".format(self.library))
        return

    def create_converter(self, library):
        if library == "pypdf2":
            return None
        elif library == "pdfminer":
            return PdfMinerParser()
        elif library == "pymupdf":
            return PyMuPdfParser()
        else:
            raise ValueError("Invalid library name")




# Usage example
# converter = PdfConverterFactory.create_converter("pypdf2")
# converter.convert_file("path/to/pdf/file.pdf")

# converter = PdfConverterFactory.create_converter("pdfminer")

s_dir = "C://Users/WMYFHCK/Downloads/technical_manuals/repair_manuals/trial_experiment/"
# s_dir = "C://Users/WMYFHCK/Downloads/technical_manuals/repair_manuals/trial_experiment/sample_file/600F 600R Repair TM2165_19_09JUL04.pdf"
# s_dir = "C://Users/WMYFHCK/Downloads/tech_manuals_one_drive/"
d_dir = "C://Users/WMYFHCK/Downloads/"

# converter.convert(s_dir, d_dir)
# records = converter.get_file_records(s_dir)
# if records is not None and len(records) > 0:
#     print(len(records))
#     print(type(records[0]))
#     print(records[0])
#     print(records[0].text)
#     print(records[0].image)

# converter = PdfToTextConverterFactory.create_converter("pymupdf")
# converter.convert("path/to/directory/with/subdirectories")
