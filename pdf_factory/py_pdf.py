# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:33:37 2023

@author: va62833
"""

# importing required modules
from PyPDF2 import PdfReader
import os


def pdf2txt(pathIN="",pathOUT=""):
    # path="C://D//New folder//pdf2txtIN//"
    # outpath="C://D//New folder//pdf2txtOUT/"
    path=pathIN
    outpath=pathOUT
    
    print(path)
    print(outpath)
    for filename in os.listdir(path):
        # outputfilename=url.split("/")[-1] # this will extract value before.html
        outputfilename=filename[:-4]
        print(filename)
        
        
        # creating a pdf reader object
        reader = PdfReader(path+"/"+filename)
        
        # printing number of pages in pdf file
        pg=print(len(reader.pages))
        print("total number of pages in given {} pdf are {}".format(filename, pg))
        outfile=filename
        line=1
        EOF_MARKER = b'%%EOF'
    
        EOF_MARKER = b'%%EOF'
        
    
        with open(path+"/"+filename, 'rb') as f:
            contents = f.read()
        
            # check if EOF is somewhere else in the file
            if EOF_MARKER in contents:
                # we can remove the early %%EOF and put it at the end of the file
                contents = contents.replace(EOF_MARKER, b'')
                contents = contents + EOF_MARKER
            else:
                # Some files really don't have an EOF marker
                # In this case it helped to manually review the end of the file
                print(contents[-8:]) # see last characters at the end of the file
                # printed b'\n%%EO%E'
                contents = contents[:-6] + EOF_MARKER
        
        # with open(filename, 'wb') as f:
        #     f.write(contents)
    
        # reader_fixed = PdfReader(outputfilename + '_fixed.pdf')
        print(reader)
        #text = textract.process(path+outputfilename+".pdf", method='pdfminer')
        print(len(reader.pages))
        l=len(reader.pages)
        
        with open(outpath+"/"+outputfilename+".txt",'w') as f:
            # print(outputfilename,file=f)
            # print("*********************",file=f)
            for line in range(0,len(reader.pages)):
                # getting a specific page from the pdf file
                # check if EOF is somewhere else in the file
                    # print("Page Number"+str(line+1),file=f)
                    # print("*********************",file=f)
                    page = reader.pages[line]
                   
                    # extracting text from page
                    #outfile = outfile+page.extract_text()
                    print(page.extract_text(),file=f)
                    # print("*********************",file=f)
            break

     

if __name__ == '__main__':
    # TODO - PyPdf library sometime gives one line per word  as pointed out in the below link
    # KNOWN ISSUE - https://stackoverflow.com/questions/52303980/pypdf2-returns-only-one-line-per-character
    path = "C://Users/WMYFHCK/Downloads/tech_manuals_one_drive"
    outpath = "C://Users/WMYFHCK/Downloads/tech_manuals_txt_one_drive"
    # pdf2txt(pathIN=path, pathOUT=outpath)