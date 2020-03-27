# Regular expressions:
import re


class ParseText():
    def parsehtml():
        """
        Parsing the html and putting relevant data in the data.txt file
        
        FIXME: A little bug:
                    Some countries have an "a" afther their name because they are
                links in the original page.
        """
        with open("data/data.txt", 'w') as data:
            with open("out.html", 'r') as html:
                lines = html.readlines()

                for line in lines:
                    line = str(line)
                    line = re.sub('[\[<>\"/;\]]', '', line)
                    line = line.strip("tbody")
                    line = line.strip("tr")
                    line = line.strip("tr style=")
                    line = line.strip("td")
                    line = line.strip("font-weight: bold font-size:15px text-align:lefta class=mt_a href=country")
                    line = line.strip("font-weight: bold text-align:right")
                    line = line.strip("font-weight: bold text-align:rightbackground-color:")
                    line = line.strip("font-weight: bold text-align:rightbackground-color:")
                    line = line.strip("xt-align:rightfont-weight:bold")
                    line = line.strip("#FFEEAA+")
                    line = re.sub('[ ]', '', line)
                    line = re.sub('[,]', '.', line)
                    line = line[:-3]

                    data.write(line)
                    data.write('\n')

    def parsedata():
        """
        Parsing the data.txt file and converting it to data.csv
        """
        dataForCSV = []
        count = 0

        with open("data/data.csv", 'w') as csv:
            with open("data/data.txt", 'r') as data:
                lines = data.readlines()

                for line in lines:
                    line = str(line)

                    if line.isspace():
                        line = "Missing"
                    else:
                        dataForCSV.append(line)
                        count += 1
                        if count == 10:
                            count = 0
                            dataForCSV = str(dataForCSV)
                            dataForCSV = re.sub('[\[\]\']', '', dataForCSV)
                            
                            csv.write(dataForCSV)
                            csv.write("\n")
                            
                            dataForCSV = list(dataForCSV)
                            dataForCSV.clear()
