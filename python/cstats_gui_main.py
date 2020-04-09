# Gather data from https://www.worldometers.info/coronavirus/
from parsehtml import TestConnection, Scrape

# Parse the data and convert it:
from parsetext import Convertor, CreateFinal

# Imports:
import logging
logging.basicConfig(filename='cstats.log', filemode='w', level='DEBUG',format='%(asctime)s - %(name)s [%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.info('Starting GUI | Tkinter')

import tkinter as tk
from tkinter import filedialog

import os

# Design:
BG_WINDOW = '#1a1b40'
TITLE_TXT = '#ffffff'
BUTTON_BG = '#26425c'
BUTTON_TX = '#ffffff'

# Button functions:
def start_batch():
    logging.debug('startBatch button pressed.')
    """ ~ Phase 1 ~ """
    TestConnection.test()

    Scrape.generateData()

    """ ~ Phase 2 ~ """
    Convertor.cleanup()
    Convertor.convert_to_csv()
    
    CreateFinal.makefile()


def view_data():
    logging.debug('viewData button pressed.')

    DATA_DIR = '../data'

    filename = filedialog.askopenfilename(initialdir=DATA_DIR, title="Select the file that you want to view")
    if len(filename) > 2:
        print("[OPENING] Please wait")
        os.system(filename)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # Title:
        self.label = tk.Label(parent, text="Coronavirus Stats", height=2, width=35, bg=BG_WINDOW, fg=TITLE_TXT)
        self.label.pack()
        # Buttons:
        self.startBatch = tk.Button(parent, text="Collect and generate data.", bg=BUTTON_BG, fg=BUTTON_TX,
                        height=3, width=34, command=start_batch)
        self.viewData = tk.Button(parent, text="View the data", bg=BUTTON_BG, fg=BUTTON_TX,
                        height=3, width=34, command=view_data)

        self.startBatch.pack()
        self.viewData.pack()
        #Footer:
        self.label = tk.Label(parent, text="Made with 💚 by David Pescariu\nOpen-source @ github.com/davidp-ro", height=2, width=35, bg=BG_WINDOW, fg=TITLE_TXT)
        self.label.pack()
        logging.info('Window generated.')


def main():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title('CStats v3.0')
    root.iconbitmap('logo.ico') # Source: https://unsplash.com/photos/EAgGqOiDDMg
    root.mainloop()


# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file
