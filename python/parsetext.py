"""
Release 3.0 | github.com/davidp-ro
"""
import re
import datetime

# Logger:
import logging
logging.basicConfig(filename='cstats.log', filemode='w', level='DEBUG',format='%(asctime)s - %(name)s [%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S')

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
        
        try:
            with open('rawdata/tableData.txt', 'r') as toClean, open('rawdata/data.txt', 'w') as cleaned:

                for _ in range(156):
                    clean.append(next(toClean))
                for line in toClean:
                    cleaned.write(line)

            logging.info('Cleanup completed') 
        except Exception as excpt:
            logging.warning('Unexpected:')
            logging.exception('Exception occured in the cleanup method')
    

    def convert_to_csv():
        try:
            with open('rawdata/data.txt', 'r') as data, open('rawdata/data.csv', 'w') as csv:
                # Header:

                csv.write("Country,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious/Critical,Total Cases/1M Pop,Deaths/1M Pop,Total Tests,Tests/1M Pop,Continent__\n")
                # Data:
                lines = data.readlines()

                count = 1

                for line in lines:
                    line = re.sub('[,]', '.', str(line))

                    if count < 15:
                        csv.write(''.join(str(line))[:-1] + ',')
                        count += 1
                    else:
                        csv.write('\n')       
                        count = 1  

                logging.info('Succesfully converted data to .csv') 
        except Exception as excpt:
            logging.warning('Unexpected:')
            logging.exception('Exception occured in the convert_to_csv method')


class CreateFinal():
    def makefile():
        DATETIME = datetime.datetime.now()
        DATETIME = str(DATETIME.strftime("%d")) + str(DATETIME.strftime("%b") + str(DATETIME.strftime("%Y"))) + '_' + str(DATETIME.strftime("%H")) + str(DATETIME.strftime("%M"))
        FILENAME = '../data/data_' + DATETIME + '.csv'

        try:
            with open('rawdata/data.csv', 'r') as csv, open(FILENAME, 'w') as final:
                lines =  csv.readlines()

                for line in lines:
                    line = str(line)[:-3] 
                    final.write(line+'\n')

            print('[INFO] CStats done')
            logging.info('CStats batch data done @ %s' % DATETIME)    
        except Exception as excpt:
            logging.warning('Unexpected:')
            logging.exception('Exception occured in the makefile method')

        logging.debug('<end of parsetext>')  

# © David Pescariu 2020 - Open-source @ github.com/davidp-ro
# License: See LICENSE file                  
