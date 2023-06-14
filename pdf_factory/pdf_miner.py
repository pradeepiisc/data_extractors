
import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
import os
import shutil
from pdf_factory.pdf_processor import PdfProcessor

class PdfMinerParser(PdfProcessor):
    def __init__(self) -> None:
        super().__init__()
        pass

    def process_directory(self, source_dir, destination_dir):
        print("Inside Process directory function")
        print("Iterating on source directory ", source_dir)
        for root, dirs, files in os.walk(source_dir):
            print("Inside for loop")
        # Create the corresponding directory structure in the destination directory
            for directory in dirs:
                source_path = os.path.join(root, directory)
                print(source_path)
                relative_path = os.path.relpath(source_path, source_dir)
                print(relative_path)
                destination_path = os.path.join(destination_dir, relative_path)
                print(destination_path)
                os.makedirs(destination_path, exist_ok=True)

            print("Total files to process are {}".format(len(files)))
            # Process the files to the destination directory
            for file in files:
                source_file = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                destination_path = os.path.join(destination_dir, relative_path, file.split("pdf")[0]+"txt")
                print(destination_path)
                # shutil.copy2(source_file, destination_path)
                print("processing {} file".format(source_file ))
                records = self.process_file(source_file)
                with open(destination_path, 'w', encoding='utf-8') as f:
                    for line in records:
                        print(line.text,file=f)
        return

    
    def process_file(self, file_path):
        print(len(self.data.records))
        ## Snipped adapted from Yusuke Shinyamas 
        #PDFMiner documentation
        # Create the document model from the file
        parser = PDFParser(open(file_path, 'rb'))
        document = PDFDocument(parser)
        # Try to parse the document
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object 
        # that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a buffer for the parsed text
        retstr = StringIO()
        # Spacing parameters for parsing
        laparams = LAParams()
        codec = 'utf-8'

        # Create a PDF device object
        device = TextConverter(rsrcmgr, retstr, 
                                
                               laparams = laparams)
        # Create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        pdf_pages = PDFPage.create_pages(document)

        for page in pdf_pages:
            interpreter.process_page(page)
                
        records = retstr.getvalue().splitlines()
        for each_rec in records:
            self.data.add_record(text=each_rec, image="")

        return self.data.records
        


if __name__ == '__main__':
    # p = MyParser(sys.argv[1])
    print("Inside Main")

    # Remember to end the path with /
    # Given the following text extracted from a pdf table delimited by triple quotes, please answer the following questions 
    base_path = "C://Users/WMYFHCK/Downloads/technical_manuals/repair_manuals/"
    input_dir = "trial_experiment"
    output_dir = input_dir + "_txt"
    p = PdfMinerParser()
    p.process_directory(source_dir=base_path+input_dir, destination_dir=base_path+output_dir)
