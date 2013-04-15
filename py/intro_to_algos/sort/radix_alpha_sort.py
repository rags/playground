from profile import profile
import sys
import random

ALPHANUM = '''  !"#$%&'() *+,- ./ 0123456789: ; <=>? @ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{ | }~'''

WEIGHTS = dict(zip(ALPHANUM, range(len(ALPHANUM))))
WEIGHTS[''] = 0
INIT_COUNTS = [0] * (len(ALPHANUM) + 1)

def digit(i, base):
    def extract(ele):
        return ele // base ** i % base
    return extract
        
@profile
def sort(arr):
    if not arr:
        return arr
    max_len = len(max(arr, key=len))
    if not max_len:
        return arr
    a = arr
    for i in range(max_len - 1, -1, -1):
        a = rearrange(a, i)
    arr[:] = a
        
def rearrange(arr, i):
    counts = INIT_COUNTS[:]
    for ele in arr:
        counts[WEIGHTS[ele[i:i+1]]] += 1
    count = 0
    for j, ele in enumerate(counts):
        count += counts[j]
        counts[j] = count
    sorted_arr = [None] * len(arr)

    for ele in reversed(arr):
        j = WEIGHTS[ele[i:i+1]]
        idx = counts[j] - 1
        sorted_arr[idx] = ele
        counts[j] = idx
    return sorted_arr


def array(n):
    lower = ALPHANUM[72: 72 + 26]
    a = [''.join(random.sample(lower, random.randint(5, 10))) for i in range(n)]
    return a
    
def main():
    n = int(sys.argv[1]) if len(sys.argv)>1 else 50000
    a = array(n)
    sort(a)
    return a

if __name__=="__main__":
    main()


        
