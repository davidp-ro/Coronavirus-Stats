"""
Release 1.1 | github.com/davidp-ro
"""
# Imports:
import sys
import re

# Logger:
import logging
logging.basicConfig(filename='cstats.log', filemode='w', level='DEBUG',format='%(asctime)s - %(name)s [%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S')

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
            logging.info('Connection succesfull.')
        else:
            print("\n[ERROR] Webpage returned %d\n" % page.status_code)
            logging.error('Webpage returned %d' % page.status_code)
            logging.error('Webpage unreacheable. Please submit an issue @ github.com//davidp-ro/Coronavirus-Stats/issues')
            logging.warning('CStats exiting - [v2.0]')
            sys.exit()


class Scrape():
    def generateData():
        try:
            soup = BeautifulSoup(page.text, 'lxml') # Get the page
            table = soup.find_all('table', attrs={'id':'main_table_countries_today'}) # Parse the html, and get data from the table

            if not table:
                logging.error('Unexpected: Table empty')
            else:
                logging.info('Parsing table...')

            with open('rawdata/tableData.txt', 'w') as data:
                for row in table:
                    data.write(re.sub('<[^>]+>', '', str(row)))
                    
                    # Log:
                    print("[Info] Data gathered.")
                    logging.info('Html was succesfully parsed into the tableData.txt file')
                    logging.debug('<end of parsehtml>')
        
        except Exception as excpt:
            print("[ERROR] Something went wrong.")
            logging.warning('Unexpected:')
            logging.exception('Exception occured in the generateData method')
            logging.warning('CStats exiting - [v2.0]')
            sys.exit()

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file
