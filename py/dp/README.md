DP diagonal loop:

| 00 | 01 | 02 | 03 | 04 |
|    | 11 | 12 | 13 | 14 |
|    |    | 22 | 23 | 24 |
|    |    |    | 33 | 34 |
|    |    |    |    | 44 |
|    |    |    |    |    |

The loop is diagonal and each outer loop should cover one diagonal row, So

1. 00 11 22 33 44 (This is optional in most cases if the 2d array is initialized with default value like 0)
2. 01 12 23 34
3. 02 13 24
4. 03 14
5. 04

Without principal diagonal:

n=5
for i in range(n-1): # [0,1,2,3] not used directly
   for j in range(n-i-1): # first index for array [0..n-i-1]
   	   print('%d%d'%(j,j+i+1),end=' ') #2nd index is always i+1 ahead of j. Ex: for i=1 case, the 2nd indexer is 2 ahead of first indexer.
   print()        


With principal diagonal:

n=5
for i in range(n): # [0,1,2,3,4] not used directly
   for j in range(n-i): # first index for array [0..n-i-1]
   	   print('%d%d'%(j,j+i),end=' ') #2nd index is always i+1 ahead of j. Ex: for i=1 case, the 2nd indexer is 2 ahead of first indexer.
   print()        


DP lookup (For a substring kind of DP):
To calculate value for (i, j) in most cases involves looking up (i, 0..j-1) (i + 1..n, j) pairs.

Ex: find minimum sum from prev subproblems

    f(04) =  min {
                 f(03) + f(44),
                 f(02) + f(34),
                 f(01) + f(24),
                 f(00) + f(14),
                 }
So the pairs for 04 are (03, 44), (02, 34) .... (00, 14)


Exclude principal diagonal:

n=5
for k in range(n-1): # [0,1,2,3] not used directly
   for i in range(n-k-1): # first index for array [0..n-i-1]
       j = i + k + 1
       m = k + 2 # lookback length
       print("%d%d: "% (i, j), end = '')
       for l in range(1, m):
           print('%d%d--%d%d'%(i,j - l, i + m - l, j),end=', ') #2nd index is always i+1 ahead of j. Ex: for i=1 case, the 2nd indexer is 2 ahead of first indexer.
   print()        


Include principal diagonal:

n=5
for k in range(n): # [0,1,2,3] not used directly
   for i in range(n-k): # first index for array [0..n-i-1]
       j = i + k 
       m = k + 1 # lookback length
       print("%d%d: "% (i, j), end = '')
       for l in range(1, m): #1..i+1
           print('%d%d--%d%d'%(i,j - l, i + m - l, j),end=', ') #2nd index is always i+1 ahead of j. Ex: for i=1 case, the 2nd indexer is 2 ahead of first indexer.
   print()        
