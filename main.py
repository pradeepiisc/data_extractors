import argparse
from pdf_extraction_factory import PdfConverterFactory
from time import time
  
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def parse_arguments():
    parser = argparse.ArgumentParser(description='PDF to Text Converter\n Example of calling - python main.py --absolute_source_file_path <PATH> --absolute_dest_path <PATH> --factory_method <METHOD>')
    parser.add_argument('--absolute_source_file_path', type=str, required=True, help='Absolute path of the source PDF file')
    parser.add_argument('--absolute_dest_path', type=str, help='Absolute path of the destination directory(NOT file!)')
    parser.add_argument('--factory_method', type=str, required=True, choices=["pypdf2", "pdfminer", "pymupdf"], help='Factory method to choose')
    args = parser.parse_args()
    source_file_path = args.absolute_source_file_path
    dest_file_path = args.absolute_dest_path
    factory_method = args.factory_method
    return source_file_path, dest_file_path, factory_method

@timer_func
def pdf_to_text(source_file_path, dest_file_path, factory_method):
    print("Insdie pdf_to_Text with {} factory method".format(factory_method))
    converter = PdfConverterFactory(factory_method)

    # Convert method automatically figurs out if its a file or a directory
    converter.convert(source_file_path, dest_file_path)
    return

@timer_func
def pdf_to_text_image(source_file_path, factory_method):
    if factory_method != "pymupdf":
        return []
    
    print("Getting both text and image records")
    converter = PdfConverterFactory(factory_method)

    # Convert method automatically figurs out if its a file or a directory
    records = converter.get_file_records(source_file_path)
    return records

if __name__ == '__main__':
    source_file_path, dest_file_path, factory_method = parse_arguments()
    # print("Found following arguments - {}, {}, {}".format(source_file_path, dest_file_path, factory_method ))

    if dest_file_path is None or dest_file_path == "":
        records = pdf_to_text_image(source_file_path=source_file_path, factory_method=factory_method)
        print("Received total {} records of both text and images".format(len(records)))

    else:
        pdf_to_text(source_file_path, dest_file_path, factory_method)
        print("Converted and stored the pdf(s) as text file(s)")