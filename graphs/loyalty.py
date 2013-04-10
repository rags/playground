import csv
from matplotlib import pyplot
from score_data import USER, VENDOR, LOY

def read():
    with open("scores.csv") as csv_data:
        reader =  csv.reader(csv_data)
        reader.next()
        data = {}
        for record in reader:
            vendor = record[VENDOR]
            user = record[USER]
            if not vendor in data:
                data[vendor] = {}
            if not user in data[vendor]:
                data[vendor][user] = round(float(record[LOY]), 1)
        return data

def histogram(data):
    for vendor in data:
        data_ =  filter(lambda x:  x > 0, data[vendor].values())
        if len(data_) > 1:
            print vendor,  data[vendor]
            pyplot.figure()
            pyplot.hist(data_, bins = 10, range = (0, 1.0), label = vendor)
            pyplot.title("Loyalty Histogram")
            pyplot.xlabel("Score (0-1)")
            pyplot.ylabel("No. of Users")
    
            pyplot.savefig("out/loyalty/%s.png" %
                           vendor.replace(".", "-").replace("/", "-").strip() or "None")

def main():
    data = read()
    #print len(data), data
    histogram(data)
    
if __name__ == '__main__': main()
    
    