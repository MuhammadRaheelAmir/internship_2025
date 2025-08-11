# Web scrapping
'''
https://www.python.org/
https://cran.r-project.org/
'''

import threading
from bs4 import BeautifulSoup
import requests

urls=[
    'https://www.python.org/',
    'https://cran.r-project.org/'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched data : {soup.text}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("The webpage has been fetched")
