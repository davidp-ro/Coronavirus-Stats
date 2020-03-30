"""
    Small project to gather data from worldometers about the COVID outbreak
and exporting it as a csv, or show graphs about it <- WIP

Release 1.1 | github.com/davidp-ro
"""

#TODO: Graphical interface, probably with kivy
#TODO: Web-page to see the results <-----> WIP

# Gather data from https://www.worldometers.info/coronavirus/
from parsehtml import TestConnection, Scrape

# Parse the data and convert it:
from parsetext import Convertor, CreateFinal

def main():
    """ ~ Phase 1 ~ """
    TestConnection.test()

    Scrape.generateData()

    """ ~ Phase 2 ~ """
    Convertor.cleanup()
    Convertor.convert_to_csv()
    
    CreateFinal.makefile()

if __name__ == "__main__":
    main()

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file
