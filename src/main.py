"""
    Small project to gather data from worldometers about the COVID outbreak
and exporting it as a csv, or show graphs about it <- WIP
"""

# Gather data from https://www.worldometers.info/coronavirus/
from parsehtml import TestConnection, Scrape

# Parse the data and convert it:
from parsetext import Convertor

""" ~ Phase 1 ~ """
TestConnection.test()

Scrape.generateData()

""" ~ Phase 2 ~ """
Convertor.cleanup()
Convertor.convert_to_csv()

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
