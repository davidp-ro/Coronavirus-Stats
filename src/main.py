"""
    Small project to gather data from worldometers about the COVID outbreak
and exporting it as a csv, or show graphs about it <- WIP
"""

#FIXME: See parsetext.py

#TODO: Graphical interface, probably with kivy
#TODO: Web-page to see the results

# Gather data from https://www.worldometers.info/coronavirus/
from parsehtml import TestConnection, Scrape

# Parse the data and convert it:
from parsetext import Convertor

def main():
    """ ~ Phase 1 ~ """
    TestConnection.test()

    Scrape.generateData()

    """ ~ Phase 2 ~ """
    Convertor.cleanup()
    Convertor.convert_to_csv()

if __name__ == "__main__":
    main()

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file
