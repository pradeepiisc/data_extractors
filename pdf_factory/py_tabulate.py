from tabula import read_pdf
from tabulate import tabulate

if __name__ == '__main__':
    # p = MyParser(sys.argv[1])
    print("Inside Main")

    # Remember to end the path with /
    # Given the following text extracted from a pdf table delimited by triple quotes, please answer the following questions 
    base_path = "C://Users/WMYFHCK/Downloads/technical_manuals/repair_manuals/"
    input_dir = "trial_experiment"
    output_dir = input_dir + "_txt"
    text_floc = output_dir + "/sample_file/600F 600R Repair TM2165_19_09JUL04.txt"
    pdf_floc = base_path + input_dir + "/sample_file/600F 600R Repair TM2165_19_09JUL04.pdf"




#reads table from pdf file

    df = read_pdf(pdf_floc, pages="all") #address of pdf file
    print(tabulate(df))