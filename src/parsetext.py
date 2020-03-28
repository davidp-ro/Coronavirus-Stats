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
            csv.write("Country,Total Cases,New Cases,Total Deaths,New Deaths,Total Recovered,Active Cases,Serious/Critical,Total Cases/1M Pop,Deaths/1M Pop,1st case date\n")
            # Data:
                
