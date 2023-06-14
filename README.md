# data_extractors
This library helps in extracting text and image data from pdfs using a factory of methods like PdfMiner, PyMuPdf. 
Currently the support is for local files and directories. 

One can either provide a source directory or a file with pdf format to convert to text format. 
Also, if one needs the text and image records, factory method should be pymupdf. 

Text and image are put in a custom Record that can be used to generate embeddings and ingested in an index like opensearch or faiss. 

Way to call - 

python main.py --absolute_source_file_path <PATH> --absolute_dest_path <PATH> --factory_method <METHOD>
