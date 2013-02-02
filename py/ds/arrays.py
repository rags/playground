import random

def make(argv):
    upper = 50000
    sorted = False
    if(len(argv)>1):
        upper = int(argv[1])
    if(len(argv)>2):
        sorted = argv[2].lower()=="true"
    return array(upper,sorted)

def array(upper,sorted=False):
    a = range(1,upper+1)
    if(not(sorted)):
        random.shuffle(a)
    return a
