import unsorted

def sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i
        while(j>0 and a[j-1]>key):
            a[j] = a[j-1]
            j -= 1
        a[j] = key

def main():
    a = unsorted.array()
    sort(a)
    return a

if __name__=="__main__":
    main()
    
