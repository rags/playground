import csv
import numpy
from matplotlib import pyplot
from score_data import USER, PP

def read():
    with open("scores.csv") as csv_data:
        reader =  csv.reader(csv_data)
        reader.next()
        pp_map = {}
        for record in reader:
            if not record[USER] in pp_map:
                pp_map[record[USER]] = int(numpy.floor_divide(
                    float(record[PP]), .2))
        return pp_map

def histogram(data):
    pyplot.figure()
    pyplot.hist(data.values(), bins = 5, range = (0, 5), label = "data1")
    #pyplot.hist(map(lambda v: 5 - v, data.values()), bins = 5, range = (0, 5), label = "data2")
    pyplot.title("Purchaing Power Histogram")
    pyplot.xlabel("Purchasing power in \$\$ rating (1-5)")
    pyplot.ylabel("No. of Users")
    pyplot.savefig("out/purchasing_power.png")

def main():
    data = read()
    print data
    histogram(data)
    
if __name__ == '__main__': main()
    
    