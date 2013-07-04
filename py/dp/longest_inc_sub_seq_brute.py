
def all_possible(a, i):
    if not a or i >= len(a):
        return []
    seqs = all_possible(a, i + 1)
    if not seqs:
        return [[a[i]]]
    newSeqs = [[a[i]]]
    for seq in seqs:
        if a[i] < seq[0]:
            newSeqs.append([a[i]] +  seq  )
        
    return newSeqs + seqs 
    

def non_decreasing_seq_brute(a):
    print a
    s =  all_possible(a, 0)
    return reduce((lambda a, b: a if len(a) > len(b) else b), s, [])

from intro_to_algos.sort.arrays import array

if __name__ == '__main__':
    print non_decreasing_seq_brute(array(10))
    print non_decreasing_seq_brute(array(30))
#    print non_decreasing_seq_brute(array(50)) #too slow
#    print non_decreasing_seq_brute(array(70))
#    print non_decreasing_seq_brute(array(100))


    
    