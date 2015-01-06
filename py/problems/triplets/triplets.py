'''0 2 1 3 4 2 3  6 5

[(0, 0), (1, 2), (2, 1), (2, 5), (3, 3), (3, 6), (4, 4), (5, 8), (6, 7)]

0 2 1 5 3 6 4 8 7

combs:

0 2 3 4 5
0 2 3 4 6
1 2 3 5
1 2 3 6

2 * 2 * 2

012
013
014
015
016
023
024
025
026
034
035
036
045
046
123
125
126
134
135
136
145
146
234
235
236
245
246
345
346


5 7


0 2 3456
1 2 356

012  3 456
012 3 56





1 2 5 3 4 5 6 7
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


arr_size = int(sys.stdin.readline())
arr = sorted(zip(map(int, sys.stdin.readline().split()), range(arr_size)))
#arr = [0, 2, 1, 3, 4, 2, 3, 6, 5]
#arr_size = len(arr)
#arr = sorted(zip(arr, range(arr_size)))
#print([arr[i][1]  for i in range(arr_size)])
greater,  lesser = [0] * arr_size, [0] * arr_size
greatest_so_far, least_so_far = [True] * arr_size, [True] * arr_size
for i in range(1, arr_size - 1):
    prev_index = i if arr[i - 1][0] < arr[i][0] else (i - 1)
    for j in reversed(range(prev_index)):
        if arr[j][1] > arr[i][1]:
            greatest_so_far[i] = False
            continue

        if (arr[j + 1][0] > arr[j][0] or arr[j + 1][1] > arr[i][1]):
            if greatest_so_far[j]:
                lesser[i] += lesser[j] + 1
                break
            lesser[i] += 1
        
for i in reversed(range(1, arr_size - 1)):
    if not lesser[i]:
        continue
    next_index = (i + 1) if arr[i + 1][0] > arr[i][0] else (i + 2)
    for j in range(next_index, arr_size):
        if arr[j][1] < arr[i][1]:
            least_so_far[i] = False
            continue
                        
        if (arr[j - 1][0] < arr[j][0] or arr[j - 1][1] < arr[i][1]):
            if least_so_far[j]:
                greater[i] += greater[j] + 1
                break
            greater[i] +=  1

#print (arr)
#print (lesser)
#print (greater)

result = 0
i = 1
while i < arr_size:
    has_dup = arr[i - 1][0] == arr[i][0]
    result += greater[i] * (lesser[i] - lesser[i - 1] if has_dup else lesser[i])
    i += 1

# Write code to compute the number of triplets as required, and store that value in 'result'

print(result)




