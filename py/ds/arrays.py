import random

def make(argv):
    upper = 50000
    sorted = False
    if(len(argv)>1):
        upper = int(argv[1])
    if(len(argv)>2):
        sorted = argv[2].lower()=="true"
    return array(upper,sorted)

def array(upper,sorted=False, lower=1):
    a = range(lower,upper+lower)
    if(not(sorted)):
        random.shuffle(a)
    return a
