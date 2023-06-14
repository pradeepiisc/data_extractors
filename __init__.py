# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:32:54 2023

@author: IKM73F4
"""


def main():

    import MultipleWebContent_Doc as mw
    import web2txt as wt
    import pdf2txt as pt
    import SingleWebContent_Doc as sw
    
    
    print("""Following process are available-
                  1-MultiWebContent
                  2-Web2txt
                  3-SinlgeWebContent
                  4-pdf2txt
                  """)
    method=input("Please enter process number: ")
    print(method)
    
    if method=="1":
        print("MultiWebContent selected")
        PathIN=input("Please enter input file path: ").strip()
        pathOUT=input("Please enter output file path: ").strip()
        mw.MultiWeb(PathIN,pathOUT)
        
        
    elif method=="2":
        print("Web2txt selected")    
        PathIN=input("Please enter input file path: ").strip()
        pathOUT=input("Please enter output file path: ").strip()
        wt.web2txt(PathIN,pathOUT)
        
    elif method=="3":
        print("SinlgeWebContent selected") 
        PathIN=input("Please enter site url: ").strip()
        pathOUT=input("Please cookiee value: ").strip()
        sw.SingleWeb(PathIN,pathOUT)
    
    elif method=="4":
        print("pdf2txt selected")     
        PathIN=input("Please enter input file path: ").strip()
        pathOUT=input("Please enter output file path: ").strip()
        pt.pdf2txt(PathIN,pathOUT)
    
    else:
        print("Invalid option selected")    
        
main()
