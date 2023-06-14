# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:15:44 2023

@author: va62833
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib.request
import html2text

def web2txt(PathIN,PathOUT):
    # Read the Excel file containing the URLs
    # path="C://G Link//web2txt//"
    # outpath="C://G Link//text//"
    path="C://D//New folder//Web2txtIN//"
    outpath="C://D//New folder//Web2txtOUT/"
    print(path+"Websitelinks.xlsx")
    print(outpath)
    x= pd.read_excel(path+"Websitelinks.xlsx",sheet_name='Sheet1')
    df = pd.read_excel(path+"Websitelinks.xlsx")
    
    # Common directory to save the Word documents
    output_directory = 'output_documents/'
    cookiee = "s_fid=72D0DD1DF4C4523D-354CA03F37454DE3; ajs_user_id=8c8a4198-a785-5c62-8b3a-b834585d63d0; ajs_anonymous_id=70e5a2a7-29b7-4cdb-8c16-f52918db9896; ASP.NET_SessionId=xwmm0eqamilmxypfjfwockmt; s_evar49=Thursday; s_evar50=Weekday; s_cc=true; s_vi=[CS]v1|323356705AB82245-40000AAFC39EC694[CE]; .AspNet.Cookies=wvenMBJ_NgSvnrGTBzwonu_KQhpx7Zfu9M8Eh4NZtQm-FS-XDNntqBIxofASM75bzVjBd8el4C7APZYBfXfN4Xp7gDJrZM7HcXZ23sAV1SDVe7FM14SjPmN6x0q8RfrCAM2gbVhsoZkalQt1X0CYhiJqk3OU_Yy1jZlf33-WrgwEvD_IpTZWZ5wfL5IEUxrlC206eT6eeQRZBuY8EVLkWbS0ZvqLt0xmsohqaLO7byIHi9eNL7EWRyroYfPqsPeGsk7Zx707ieW4jDX1Z2XPD34RUNFiTaROaMdflCdK1IPx9St_Uta56nTj9BzsPxAESpdq_FLobrXmZZhCZLC25RhjhtBTK5R28O1PiuYfzz4CjsUk8ngc0JR9ixrhUV9Qe_itHcDqzKnDqxPhN0LliiMN4oCwrtwTeNDZbEgsmmMFeM-B_Z_ZIiKu71ta6j8IABOZ-FyN6lvvPBBjCLvk-0EHLq9_D-XV9uGgCUxb805B12jmeCsXqoGPA4VNqTQM_pA2xEMMOTz7D4GWQJZ71EBonkzjXh6GQnEr8qxUOITIzcfaBzlzZe_xfwOjUF2k8nCPSBrzQNcdXfjPfndVtw6e5HBTt2aecKF2ancI4kGKm_yW5tYewAfCKNDDkqRGGdrC6R45pTnPr0V6DGfbUzNLL2JLJ6I5em4qIhJ3wdwsXci30UkoagUn6IroUBuOJeeuUTRhU_MwzCyZNnCeuTOA-ZYTaHAMJmgNfd0DnXwkquxeDGQFuaq7OHM4FQmEfhk3KpggXn8rkBil_FVuM6RPyhTHPBTiDyOp_1xGgq73zo30u5qHdJBr8PPQw3ynYcmZ--xnlU3zqhYV1XodL1c4nHaJp7NJt-KjX8F8PXqj_XbzcyLzxOTd6Ld_-tv1ax-5OtOExYae_bYmse0chNJD852I6dCJtBAeIfEDzlRKWnTvyI03piNOd-FNeeVsgKtd62A9lgoKAYLppR927kT3Hrke4BwXDBk4106H3LWfDS1__4eEUL3KNSpXUH4Q_YjvR_28nrN8FiTcSPED2NdbPheD1vRU1XHmy2Kcg0D3j1ortHRD_4tnrBfqFAg1fZyx1JbP7OqmXf7CIl59JLdbPQngJlH3zXJ4e8ikA53aUnzRLArC-IVmkP7pS_UD4oX3XAqmajIh8_AKynqnsgmJwEjSK-d_V9X1VW28ARrrX8LXkEcErSzk2zsAdmeGznBYA2baOqso_9IJSKiF339byqZumw-hBrVC-eQ6NcpR2VvpV4WLtfAJt62n_RWn6yQgqcoOkiuXfjMbV0WKbp8Bb8G3wdi8i0xHuqzrhC9xcnMko1YjiPeroxYKK7uZKUuoun8J7Il4WalQpHHbpLPGQl11hmBsep4rN5tvEX9uqeqU_10y-h-7fvLAJVknoc_0ZmOgGjG5nW6MDNg5Jg_XFWDrImSgYkjiZaIzHJZuqmJSAmvOlcPH9YDf7LN_ZcqTwDtm39uNYk1M-anDT9brBudlxVWibAukPWOmVbhnMfIeX5W6HLQC7ZqdWx_lztgYav3A9VO0sb-Ise7cwashW3ONwJrldP6dgKN3bHyRmdTdmt32MYH-MJjHlJ_r_DM0Sk5q8goXndO6GN0StiTBp3TEf0VLuo699K3eBao; s_lv=1684464648472; s_lv_s=Less%20than%201%20day; s_evar47=Less%20than%201%20day; s_getNewRepeat=1684464648475-Repeat"
    # Iterate over the URLs
    for index, row in df.iterrows():
        url = row['Links']
        outputfilename=url.split("/")[-1] # this will extract value before.html
        outputfilename=outputfilename[:-5]
        print(outputfilename)
        print(url)
        # Send a GET request to the website and retrieve the HTML content
        #response = requests.get(url)
        response = requests.get( url,cookies = {'cookie' :cookiee})
        htmlcontent = response.text
        print(htmlcontent)
    
    # here we have to pass url and path
    # (where you want to save your text file)
    #urllib.request.urlretrieve(url,cookies = {'cookie' :cookiee})
    #						"/home/gpt/PycharmProjects/pythonProject1/test/text_file.txt")
    
    #file = open(outpath+outputfilename+".txt", "r")
    #contents = file.read()
        #page = urllib2.urlopen(url)
        #html_content = page.read()
        f = open(outpath+outputfilename+".txt", "w")
        rendered_content=html2text.html2text(htmlcontent)
       # page = urllib2.urlopen(url)
        file = open(outpath+outputfilename+".txt", 'w')
        file.write(rendered_content)
        file.close()
