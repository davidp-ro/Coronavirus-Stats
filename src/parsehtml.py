"""
Release 1.1 | github.com/davidp-ro
"""
# Imports:
import sys
import re

# Requests:
import requests

# Parser
import lxml

# BeautifulSoup
from bs4 import BeautifulSoup

# Website:
page = requests.get("https://www.worldometers.info/coronavirus/")


class TestConnection():
    def test():
        if page.status_code == 200:
            print("\n[Connected]")
        else:
            print("\n[ERROR] Webpage returned %d\n" % page.status_code)
            sys.exit()


class Scrape():
    def generateData():
        try:
            soup = BeautifulSoup(page.text, 'lxml') # Get the page
            table = soup.find_all('table', attrs={'id':'main_table_countries_today'}) # Parse the html, and get data from the table

            with open('rawdata/tableData.txt', 'w') as data:
                for row in table:
                    data.write(re.sub('<[^>]+>', '', str(row)))
                    print("[Info] Data gathered.")
        except:
            print("[ERROR] Something went wrong.")
            sys.exit()
