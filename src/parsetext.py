import re

#FIXME: China shows up at the end of the table only?
#FIXME: Each row has 2 commas due to the empty lines abw them and the way I parse the text

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
        
        with open('data/tableData.txt', 'r') as toClean, open('data/data.txt', 'w') as cleaned:
            for _ in range(18):
                clean.append(next(toClean))
            for line in toClean:
                cleaned.write(line)
    

    def convert_to_csv():
        with open('data/data.txt', 'r') as data, open('data/data.csv', 'w') as csv:
            # Header:
            csv.write("Country,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious/Critical,Total Cases/1M Pop,Deaths/1M Pop,github.com/davidp-ro,1st case date\n")
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
                    
