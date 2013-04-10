#import csv
#import numpy
from matplotlib import pyplot


def draw():
    pyplot.figure()
    pyplot.plot(range(0, 1001, 10), [score(i, 1000) for i in range(0, 1001, 10)], 'g')
    pyplot.plot(range(0, 2001, 20), [score(i, 2000) for i in range(0, 2001, 20)], 'b')
    pyplot.plot([(score(i, 1000) * .5 + score(j, 2000) * .5)
                 for i in range(0, 1001, 20) for j in range(0, 2001, 40)], 'r')
#    for i in range(0, 1001, 10):
 #       pyplot.plot(i, score(i, 1000), 'g')
    #for i in range(0, 2001, 20):
    #    ax.plot(i, score(i, 2000), 'b')
    #for i in range(0, 1001, 10):
    #    for j in range(0, 2001, 20):
    #        ax.plot(score(i, 1000) * 0.5 + score(j, 2000) * .5, 'r')
    #print sorted(dir(ax))
    pyplot.show()    
#    pyplot.savefig("out/foo.png")



DEPRECIATION_YEARLY = .8
DEPRECIATION_MONTHLY = DEPRECIATION_YEARLY ** (1.0 / 12)

def score(value, max_value, min_value=0, good_checkin_factor=3, good_checkin_score=0.7):
    value =  value or 0.0
    max_value =  max_value or 0.0
    if max_value == 0.0:
        return 1.0 if value > 0.0 else 0.0
    good_score = min_value + (max_value - min_value)*1.0/good_checkin_factor
    if(value<=good_score):
        return keep_in_bounds(good_checkin_score * (value - min_value)*1.0/(good_score - min_value))
    else:
        return keep_in_bounds(good_checkin_score + (1-good_checkin_score)*(value-good_score)*1.0/(max_value-good_score))

def keep_in_bounds(value):
    return 0.0 if value < 0.0 else 1.0 if value > 1.0 else value



    
def main():
    draw()
    
if __name__ == '__main__': main()
    
    