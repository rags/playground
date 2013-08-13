text=raw_input()
words=[raw_input() for i in range(int(raw_input()))]
def is_valid(c):
    return c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
def bin_insert(a,e,lo=0,hi=None):
    hi=hi or len(a)
    mid=(hi+lo)//2
    if hi==lo+1:
        a.insert(hi if e>a[lo] else lo,e)
        return    
    if a[mid]>e:
        bin_insert(a,e,lo,mid)
    else:
        bin_insert(a,e,mid,hi)
        
valid_text=filter(is_valid,text)
all_words = valid_text.lower().split(' ')
indices=dict(zip(words,[[] for i in words]))
for i,word_sentence in enumerate(all_words):
    
    for word in words:
        if word==word_sentence:
            indices[word].append(i)
arrs = indices.values()
if any(not arr for arr in arrs):
    print "NO SUBSEGMENT FOUND"
else:
    idxs=[0 for i in arrs]
    min_range=None
    eles = sorted([(arrs[i][j],i) for i,j in enumerate(idxs)])
        
    while True:
        if not min_range or min_range[1]-min_range[0]>eles[-1][0]-eles[0][0]:
            min_range=eles[0][0],eles[-1][0]
        inc=False
        for k,(_,i) in enumerate(eles):
            if idxs[i]<len(arrs[i])-1:
                inc=True
                idxs[i]+=1
                eles.pop(k)
                bin_insert(eles,(arrs[i][idxs[i]],i))
                break
        if not inc:
            break
    #print min_range
    print ' '.join(valid_text.split(' ')[min_range[0]:min_range[1]+1])