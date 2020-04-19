"""
    This is the main script that has to be added to the pyinstaller.

    Build:
        pyinstaller pyinstaller --add-data="logo.ico;res" --add-data="main.py;src" --add-data="parsehtml.py;src" --add-data="parsetext.py;src" --add-data="cstats_gui_main.py;src" run_cstats.py
    Result:
        in the dist folder -> look for .exe

    CStats v3.1
"""
import os

if __name__ == "__main__":
    #print("run")
    os.system('python main.py -gui')

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file