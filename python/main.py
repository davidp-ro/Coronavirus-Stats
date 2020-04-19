"""
    Small project to gather data from worldometers about the COVID outbreak
and exporting it as a csv, or show graphs about it <- WIP

Release 3.1 | github.com/davidp-ro
"""

#TODO: Web-page to see the results <-> WIP

import sys

def main():
    try:
        if sys.argv[1] == '-no_gui':
            # Gather data from https://www.worldometers.info/coronavirus/
            from parsehtml import TestConnection, Scrape

            # Parse the data and convert it:
            from parsetext import Convertor, CreateFinal

            """ ~ Phase 1 ~ """
            TestConnection.test()

            Scrape.generateData()

            """ ~ Phase 2 ~ """
            Convertor.cleanup()
            Convertor.convert_to_csv()
            
            CreateFinal.makefile()
        
        elif sys.argv[1] == '-gui':
            from cstats_gui_main import main
            main() # Running tkinter for gui

    except IndexError:
        print("[ERROR] main.py takes an argument!")
        print("Usage: -gui if you want to run with a GUI, or -no_gui to run in the CLI")


# CStats v3.0
if __name__ == "__main__":
    main()

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file
