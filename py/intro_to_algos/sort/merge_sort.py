import unsorted,sys

def sort(a):
    merge_sort(a,0,len(a),[0]*len(a))

def merge_sort(a,start,end,result):
    if(end - start < 2):
        return
    mid = (start + end)//2
    merge_sort(a,start,mid,result)
    merge_sort(a,mid,end,result)
    i,j=start,mid
    k=0
    while(i<mid and j<end):
        if(a[i]<a[j]):
            result[k], i = a[i], i+1
        else:
            result[k], j = a[j], j+1
        k += 1
            
    while(i<mid):
        result[k] = a[i]
        i,k = i+1,k+1
    i,j = start,0    
    while(j<k):
        a[i], i, j = result[j], i+1, j+1
 

def main():
    a = unsorted.array()
    sys.setrecursionlimit(len(a)**2)
    sort(a)
    return a

if __name__=="__main__":
    main()
    
