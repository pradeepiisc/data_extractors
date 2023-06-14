# -*- coding: utf-8 -*-
"""
Created on Fri May 19 14:32:54 2023

@author: VA62833
"""

import requests
from bs4 import BeautifulSoup
from docx import Document

def SingleWeb(url,cookiee):
    
    # URL of the website you want to import text from
    #url = "https://dlrdoc.deere.com/sales/salesmanual/en_NA/tractors/2023/feature/transmissions/6r/powerquad_autoquad_r4_t4.html"
    #"https://www.deere.com/en/mowers/lawn-tractors/100-series/"
    
    
    #url = "http://dlrdoc.deere.com/sales/salesmanual/en_NA/seeding/2019/feature/fertilizer/liquid_fert_row_accuracy.html"
    # url = "https://dlrdoc.deere.com/sales/salesmanual/en_NA/utility_vehicles/2018/feature/wheels_tires/tires_xuv590_xuv560.html"
    # cookiee = "s_fid=0A4323403B8A29A6-2B74DB5022E5B3D1; s_vi=[CS]v1|322874E173BDD5D8-400000328FB0F93D[CE]; s_ecid=MCMID|42427955768787763482650525638307254639; _gcl_au=1.1.2088816943.1684343218; _fbp=fb.1.1684343218140.723479145; __qca=P0-1804714339-1684343219565; ASP.NET_SessionId=czyzffij0vyrpcvx3xgzwvuo; s_evar47=Less than 1 day; s_evar50=Weekday; s_cc=true; at_check=true; mbox=PC#53f3d3d432b64508a0fd0eb55ac01310.34_0#1747588018|session#547c932ec710447985467934fa8102e0#1684504039; AMCVS_8CC867C25245ADC30A490D4C@AdobeOrg=1; AMCV_8CC867C25245ADC30A490D4C@AdobeOrg=179643557|MCAID|322874E173BDD5D8-400000328FB0F93D|MCIDTS|19497|MCMID|42427955768787763482650525638307254639|MCOPTOUT-1684509378s|NONE|MCAAMLH-1685106978|7|MCAAMB-1685106978|j8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI|MCSYNCSOP|411-19502|MCCIDH|51983634|vVersion|5.5.0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+May+19+2023+18:46:20+GMT+0530+(India+Standard+Time)&version=202304.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=88fdd41c-1bf5-4451-93e6-f090844f27f2&interactionCount=1&landingPath=https://www.deere.com/en/mowers/lawn-tractors/100-series/&groups=C0001:1,C0003:1,C0004:1,C0002:1; s_ips=657; s_tp=7247; s_ppv=en_us%20%3A%20mowers%20%3A%20lawn-tractors%20%3A%20100-series,9,9,657,1,11; .AspNet.Cookies=PI8G6ENG-JPHgyCzWL2YUIRqwkWwUmWBisHay6kbvt9-NT_hPFhptpLdfngeyG-w5li5BnkMxoTY7mf_LB_Cr-WdNHjcxmnRXEEPNddqQrTfWxzPtQ4GN6hCIgrSIYowNBc858gC-_v7QT4aRjES6DMx7NN8OLKGdZM-oPYZuQ2we45mZHIiWMDGFWpfBQyYp79HNI4AcTg-NE1g1YI14Ot0FhNS_9rhgkxVphi8NDMUwnRisZS98fxQkwmNV17v0L0R6v8-OPj8tD8v_ybrdpfZ7z05AGyOWJMRMwXK8o7HHfH3QUHPiBmq5pSI9nC5piMZ5BEc7fGSk6zU67tB_cC7SPI4hK1inQjaSbTFIr2mbsmeo2TqzzuIsxK_UIHVpLehN3dQOMfXljpntVJ521RpwgJj_PnG_QFewxRSYQucZvQ5ftZFYlt2FydDgNwrqzg5h8fj5_IHAfNi1AtOvCsZcG50mVQuJFeVZvZwA8g2V8E_oV5QjUvkSPlS1z-Th0ZnVpprALkzlVVinRRNHJ4foyYMW4K8Oxn-2TEoVovg0usOTbncTqfDJAsIBWi0mGYzVs1wrJxFLlLCLYFdgm8xQcFI-fLlEES40IWQPNB-WqB5NiGmZh2W2HAJkaOHqJiO1BLnO2deMtkoR5xkMpHga_aNVDZC8XRLeXkD5V3GULJsdgniSTsexvwz1yMn00iDSlXeG_aQh18ZkiKslqBeuckgOO9njGLjevtwmaSgMcHwU-0nRly_kbxeI4QBihwCroE-1r4Qz9rRjiHsbs39nzmcBV1aio_foNFRQ0I2xDY3LhLoJkAqslFq4_0Qj5UC0lNvYp0NEUBp-6XZMq-8GOZsHjLhCNwNwHDZZf__jgJw-JKQjkVdatxDslceG3hFTqLX7Cw3ERgsB8_VEsTmkKphCfX64q916GDyBcuJrIdcBjquGXwfoe1zp6MVx7OIsR9WzZeOw4F8aHPeVeWQ1ys-9qR0cfd3qgzywsXe5BOvqf2wkK-jQrou01irt0BipfTkKItAjhN2DFZyhseGfmHGQ4WATS_OFFQ4Gn5IpIriAWFbo2g-EhhAfE2yzaouKdn4Unf-FVuyMk-Cktj6X50ufrOBFII5CFSCF4P8b3OaxWYED2eXpaXEK0cqbyMc-a7ZUDEnE2qbNDOOwwchUf6xK5tAQpfopBKPOxnHKxO-KrGrjGvwfcwx1JJeLtq7-gYesIJoxpAgjNo6lxJYzc4dUsgvWwP5XgHLEtXmbYW_EmIYgm9HEKuAN221_wCKzinL57uzfYt8kB4yRAf_uKINkiXwZFehUdNccPUUrqYfxLRxnE0eg58eeF3tbek93h0JP5zYiFX2tXbi4It5gvBkwpyjyjZ_312Ah4fGkDJo-MgqiOTQVBhA8oZgsl_3DlkNd_fLZqMxt1W7xZi_XeCL9UMOS1aat0KlH8OozdChgaM6dk_QktxeXJmxMfsSc7xhnYULyWCp-tYvAst8jkea9OSDdHkDNju-xznTfCT4UEVRHD9fcK-1-MtYHpmC7hoqV5GfYH3iWDUjYr1Io3PhrajRa53IRZ7LeUAjDOPUl7RUwBCF470Yk85E; s_lv=1684502961329; s_lv_s=Less than 1 day; s_evar49=Friday; s_getNewRepeat=1684502961337-Repeat"
    
    url=url
    cookiee=cookiee
    # Send a GET request to the website and retrieve the HTML content
    response = requests.get( url,cookies = {'cookie' :cookiee})
    
    #response = requests.get(url)
    html_content = response.text
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract the text from the website
    text = soup.get_text()
    
    # Create a new Word document
    document = Document()
    
    # Write the extracted text into the Word document
    document.add_paragraph(text)
    
    # Save the Word document
    document.save("website_text.docx")