# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:32:54 2023

@author: VA62833
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from docx import Document

def MultiWeb(pathIN,pathOUT):
    # Read the Excel file containing the URLs
    # path="C://G Link//"
    # path="C://D/New folder/"
    # outpath=r"C://D//New folder//MultiwebOUT/"
    path=pathIN
    outpath=pathOUT
    print(path+"Websitelinks - Copy.xlsx")
    print(outpath)
    x= pd.read_excel(path+"Websitelinks - Copy.xlsx",sheet_name='Sheet1')
    df = pd.read_excel('Websitelinks - Copy.xlsx')
    
    # Common directory to save the Word documents
    output_directory = 'output_documents/'
    cookiee = "s_fid=72D0DD1DF4C4523D-354CA03F37454DE3; ajs_user_id=8c8a4198-a785-5c62-8b3a-b834585d63d0; ajs_anonymous_id=70e5a2a7-29b7-4cdb-8c16-f52918db9896; ASP.NET_SessionId=xwmm0eqamilmxypfjfwockmt; s_evar50=Weekday; s_cc=true; s_vi=[CS]v1|323356705AB82245-40000AAFC39EC694[CE]; s_evar47=Less%20than%201%20day; s_evar49=Friday; .AspNet.Cookies=Rt7O0iofCsS7ciQE5vIxzcXqQU5FDUqAFQTreaRF5jCnQghprqDRbjHyUWX13rLYmFZIm16dJ9bzEi9pd7j5uoSiau8CjKakzkvEOV3YIWaXQqSAbVedFLd9KiusrN7cbf9ce6Bp0SVMEOb0iJBOjsrglMv_QjH8T2p1TMLolk_AeqTXztqqaHHrM7RD-5sR6cf-rqbC4giGsD8YAebp1Vo7pDPKMMUwVEqFKwPgoW_CFlpLblOFlDgmvXdipmDjfVEFJlt6JFjE58Wq3nj8rlyAhf929j6z0FBMp5n7nxoW9KrZPcnrDvvUBofSM4PnMzQ1wKoyCps6hxJKs8Z1jlwwpMy0ocGt2-6IbMW3HabLsyhBckUZ_h6gT-heXkJiJeiJcYQTpCdFS1zwWgTGpP3M3j49l5NpQbnPcopCXvpFDomHdVO2jhc0ucvD8USVIJQ_CMQRu7Ixj6TcIyY73F054Xeb7ryfZ8GBgdiB8P_0UOIrniA_erYcIUQVf2CJx8nJArVMwLdVoGBicV3j31nKNVMEaJuwbqI-wBBXUGNFfLOnXQdUf9MWiQjAGFcqYJfxdkljdE8b-IwdOYnW_T1VYtpwYZXY3FlW0mZFvSuPazZfqP8EhsRZpCavLMvngf71fcCpp-cXR3G2IxaNK1f7Py6BOGAdh0KDeFmCQMNbfasfVgEY5QaT6FHgl5Du6-d751r2NObAejZoQtciKyCShY8Av2K_PgYugtcjIhGBWWcYPLvSj1_HdVYuecpLuJO97VL6q9RTTmwuc6Zq9KyVJBHIjrrylF4EUF2g4FeXsuUw1iOOuebGkfjSBujK9VxPwqwYV7O7_p-HFgjsvWZC8rLbf9b3OJgDEnSNq06Zj4I-ZxxOwSA9kize-3CFAHujrSYiJkiBa4EJRhBmKHHtnY2IDYOXpMIq6r5EMJL-gbzFiBAYNfk1BUZ2gKHFGmQEYGHUXy8zG6SUXYGdA1FenLX-wOG4Aa5DlhxRvyOC2A08_t54K4cInQTmtvkfz2rfUX6FTFsFg7t21RJ276-dpNgVzxXlO4cTc0OSNkdh1QhP-5g_phV3fMBr8awvOappg5qWfxEcxf2wn08e1BjQ8aFeaVvwlJWanZ1babYIk06WEvxgb8UP_U4ae19fgINlhn2XJF-aZP8lFXHbai_D3Q2srgoMa57ftoXYLyqhB_IoK2-kNjsYVwMnmxkIc7EUa7mdZkHdf4quOeWaJzB0ftnZQYXtQI8aBTIkYVwfdLoOquEF7OgoyaeQ2PLj2yn3dLZrKrXrfKiZLOetOV1GP0oefifP_yVv96Fr1FXuiuHHc2Pxi7ysPBRMGojSxvYhi9vndIGLV1N0Prg-lzV4CjnXUzC-lNHsDshPn27G8tS5mg-VryGBOj3BSVpvkillgHzAw_glYE1N4dnei5wSMcgcEAmJN6Jkhrr4NCTVLHgDtjuqEhRtyit69OqKNv23QTAuBoXYzSdV5bUzI4V20wFjh0dxfX0mQJWuQnnE3QFG7dx8_AIS0R3Jst41nchjnybhp-SJddE6Fg3eS0cjjApnB_PM2Tah7jOCveMFS0KffM5Fr0VOVvqAOjZHZ7ulm-RbhNXMYHnzZaT-Eq_5idMaI-5C7jtf35x_IGtWf6sGq_lQiPukmKrSU372LljejWv7hF59pttFVq9giw; s_lv=1684511730247; s_lv_s=Less%20than%201%20day; s_getNewRepeat=1684511730251-Repeat"
    # Iterate over the URLs
    for index, row in df.iterrows():
        try:
            url = row['Links']
            outputfilename=url.split("/")[-1] # this will extract value before.html
            outputfilename=outputfilename[:-5]
            # print(outputfilename)
            # print(url)
            # Send a GET request to the website and retrieve the HTML content
            #response = requests.get(url)
            response = requests.get( url,cookies = {'cookie' :cookiee})
            html_content = response.text
        
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(html_content, "html.parser")
        
            # Extract the text from the website
            text = soup.get_text()
        
            # Create a new Word document
            document = Document()
        
            # Write the extracted text into the Word document
            document.add_paragraph(text)
        
            # Generate the output file name based on the URL
            filename = f"{outputfilename}.docx"
        
            # Save the Word document in the output directory
            #document.save(output_directory + filename)
            
            document.save(outpath+filename)
                
        except:
            print(f"Error in url processing {filename}")
            pass            