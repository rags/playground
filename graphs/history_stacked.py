import csv
import random
from matplotlib import pyplot
from score_data import USER, CAT, HIST


def read():
    with open("scores.csv") as csv_data:
        reader =  csv.reader(csv_data)
        reader.next()
        data = {}
        for record in reader:
            category = record[CAT]
            user = record[USER]
            if not category in data:
                data[category] = {}
            if not user in data[category]:
                data[category][user] = round(float(record[HIST]), 1)
        return data

def histogram(data):
    pyplot.figure()
    for category in data:
        print category,  data[category]
        pyplot.hist(filter(lambda x:  x > 0, data[category].values()), bins = 10, range = (0, 1.0), label = category,  alpha =  random.uniform(0.0, 1.0),  histtype = 'barstacked')
        pyplot.title("History Histogram")
        pyplot.xlabel("Score (0-1)")
        pyplot.ylabel("No. of Users")
    pyplot.savefig("out/history.png")

def main():
    data = read()
    #print len(data), data
    histogram(data)
    
if __name__ == '__main__': main()
    
    