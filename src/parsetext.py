"""
Release 1.1 | github.com/davidp-ro
"""
import re
import datetime

class Convertor():
    def cleanup():
        """
            Removing the first couple of lines, because we're not interested
        in the header of the table.

          Header should contain:
            Country, Total Cases, New Cases, Total Deaths, New Deaths, Total Recovered,
        Active Cases, Serious/Critical, Total Cases/1M Pop, Deaths/1M Pop, 1st case date.
        """
        clean = []
        
        with open('rawdata/tableData.txt', 'r') as toClean, open('rawdata/data.txt', 'w') as cleaned:
            for _ in range(18):
                clean.append(next(toClean))
            for line in toClean:
                cleaned.write(line)
    

    def convert_to_csv():
        with open('rawdata/data.txt', 'r') as data, open('rawdata/data.csv', 'w') as csv:
            # Header:
            csv.write("Country,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious/Critical,Total Cases/1M Pop,Deaths/1M Pop,github.com/davidp-ro,1st case date__\n")
            # Data:
            lines = data.readlines()

            count = 1

            for line in lines:
                line = re.sub('[,]', '.', str(line))
                if count < 14:
                    csv.write(''.join(str(line))[:-1] + ',')
                    count += 1
                else:
                    csv.write('\n')       
                    count = 1   


class CreateFinal():
    def makefile():
        DATETIME = datetime.datetime.now()
        DATETIME = str(DATETIME.strftime("%d")) + str(DATETIME.strftime("%b") + str(DATETIME.strftime("%Y"))) + '_' + str(DATETIME.strftime("%H")) + str(DATETIME.strftime("%M"))
        FILENAME = 'data/data_' + DATETIME + '.csv'

        with open('rawdata/data.csv', 'r') as csv, open(FILENAME, 'w') as final:
            lines =  csv.readlines()

            for line in lines:
                line = str(line)[:-3] 
                final.write(line+'\n')     
                    
