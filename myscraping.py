from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import bs4
from bs4 import BeautifulSoup
import re

def spotify(playlist):
    try:
        html = urlopen(playlist)
    except HTTPError as e:
        print(e)
    except URLError:
        print("Server down or incorrect domain")
    else:
        res = BeautifulSoup(html.read(),"html5lib")
        tags = res.findAll("span", {"class": "track-name"})
        
        title = res.findAll("title")
        
        for t in title:
            name = t.getText()

        name = f"{name}.txt"
        #print(name)
        arquivo = open(name, 'w')    
        for tag in tags:
            print(tag.getText())
            arquivo.write(tag.getText() + "\n")          

        arquivo.close()
    return(name)