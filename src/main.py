"""
    Small project to gather data from worldometers about the COVID outbreak
and exporting it as a csv, or show graphs about it
"""

# Gather data from https://www.worldometers.info/coronavirus/
from gethtml import GetHTML

# Parse the data and convert it:
from parsetext import ParseText

GetHTML.test()
GetHTML.makeOutput()

ParseText.parsehtml()
ParseText.parsedata()