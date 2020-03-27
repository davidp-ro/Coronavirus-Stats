import sys

# Requests:
import requests
page = requests.get("https://www.worldometers.info/coronavirus/")

# Parser
import lxml

# BeautifulSoup
from bs4 import BeautifulSoup

class GetHTML():
    def test():
        if page.status_code == 200:
            print("\n[Connected]")
        else:
            print("\n[ERROR] Webpage returned %d\n" % page.status_code)
            sys.exit()

    def makeOutput():
        soup = BeautifulSoup(page.content, 'lxml')

        # Put the county data in a file:
        with open("out.html", 'w') as toWrite:
            toWrite.write(str(soup.find_all('tbody'))) 
            print("[Succes] COVID 19 Country data gathered.\n")  
