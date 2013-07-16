# Find longest alternating subsequence
# A seq x0,x1,x2,x3... is alternative
# if x0>x1 and x1<x2 and x2>x3
#              OR
#    x0<x1 and x1>x2 and x2<x3

def las(a):
    n = len(a)
    subseqs = [None] * n
    for i in range(n - 1, -1, -1):
        choices = [a[i: i + 1]]
        for j in range(i + 1, n):
            if (len(subseqs[j]) < 2 or
                cmp(a[i], a[j]) == -cmp(subseqs[j][0], subseqs[j][1])):
                choices.append(a[i: i + 1] + subseqs[j])
        subseqs[i] = max(choices, key=len)
    return max(subseqs, key=len)


############################## TESTS ##############################


def should_find_longest_alternating_seqs():
    assert [1] == las([1])
    assert [1, 2] == las([1, 2])
    assert [1, 3] == las([1, 2, 3])
    assert [1, 6, 2, 4] == las([1, 5, 6, 2, 4])
    assert [5, 4, 6, 3, 7, 2, 8, 1] == las([5, 4, 6, 3, 7, 2, 8, 1])
    assert ([1, 4, 1, 5, 2, 7, 4, 9, 2, 7, 4] ==
            las([1, 3, 4, 1, 3, 5, 2, 7, 4, 9, 4, 2, 7, 4]))
            