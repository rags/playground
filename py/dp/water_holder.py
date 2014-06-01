'''
The problem is to find the amount of water that can be held in these structures

|         
|       |
|   |   |
|   |   |       |     
|   |   |   |   |  |  |
-----------------------
5   3   4   1  2   1  1

The numbers denote height which is directly proportional to amount of water that can be filled.
Assume for ex: height 1 = 1L, so between walls of height 5,3, the total height is 3 and 3L of water can be held.
What is the total capacity of this structure?

In the above case its
  4*2   +  2*2  +  1*2  =  14

|                     |  
|       |             |
|   |   |             |
|   |   |       |     |
|   |   |   |   |  |  |
-----------------------
5   3   4   1  2   1  5

5*6=30

                      |  
|       |             |
|   |   |             |
|   |   |       |     |
|   |   |   |   |  |  |
-----------------------
4   3   4   1  2   1  5

4*6=24
 
  
              |            
           |  |  |         
        |  |  |  |  |      
     |  |  |  |  |  |  |   
  |  |  |  |  |  |  |  |  |
  -------------------------
1 + 2 + 3 + 4 + 4 + 3 + 2 + 1 = 20

|                       |
|  |                 |  |
|  |  |           |  |  |
|  |  |  |     |  |  |  |
|  |  |  |  |  |  |  |  |
-------------------------
5*8=40


'''
from collections import namedtuple

############################## Common ##############################
Section = namedtuple('S', 'left right len')

def merge_sections(left, right):
    llast, rfirst = left[-1], right[0]
    if (llast.left >= llast.right and llast.left >= rfirst.left and
        rfirst.right >= rfirst.left and rfirst.right >= llast.right):
        return (left[:-1] + [Section(llast.left, rfirst.right, llast.len + rfirst.len)] + right[1:])
    return left + right

def calc_capacity(sections):
    capacity = 0
    for left, right, len in sections:
        capacity += len * min(left, right)
    return capacity

############################## Recursive ##############################

def capacity_recur(*walls):
    sections = sections_recur(*walls) 
    return calc_capacity(sections)

def sections_recur(*walls):
    return _sections_recur([Section(*params) for params in  zip(walls, walls[1:], [1] * (len(walls) - 1))])
    
def _sections_recur(sections):
    if len(sections) == 1:
        return sections
    newsections = []
    for i in range(1, len(sections)):
        newsections.append(merge_sections(_sections_recur(sections[:i]),
                           _sections_recur(sections[i:])))

    return min(newsections, key=len)
        
############################## dp ##############################
    
def capacity_dp(*walls):
    return calc_capacity(sections_dp(*walls))
    
def sections_dp(*walls):
    n = len(walls) - 1
    dp_table = [[None for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n - k):
            j = i + k
            if i == j:
                dp_table[i][j] = [Section(walls[i], walls[j + 1], 1)]
                continue
            dp_table[i][j] = min([merge_sections(dp_table[i][j - l], dp_table[i + k - l + 1][j])  for l in range(1, k + 1)], key = len)
    return dp_table[0][-1]
    
if __name__ == '__main__':
    capacity_recur(5, 3, 4, 1, 2, 1, 5)

############################## TESTS ##############################

def should_calculate_capacity():
    assert capacity_dp(1, 2, 1, 1, 2, 1, 1) == 9
    assert capacity_dp(4, 3, 4, 1, 2, 1, 5) == 24
    assert capacity_dp(5, 3, 4, 1, 2, 1, 5) == 30
    assert capacity_dp(5, 3, 4, 1, 2, 1, 1) == 14
    assert capacity_dp(1, 1, 1, 1, 2, 1, 1) == 6
    assert capacity_dp(1, 2, 3, 4, 5, 4, 3, 2, 1) == 20
    assert capacity_dp(5, 4, 3, 2, 1, 2, 3, 4, 5) == 40

def should_calculate_sections():
    assert sections_dp(4, 3, 4, 1, 2, 1, 5) == [Section(4, 5, 6)]
    assert sections_dp(1, 2, 1, 1, 2, 1, 1) == [Section(1, 2, 1), Section(2, 2, 3), Section(2, 1, 2)]
    assert sections_dp(5, 3, 4, 1, 2, 1, 5) == [Section(5, 5, 6)]
    assert sections_dp(5, 3, 4, 1, 2, 1, 1) == [Section(5, 4, 2), Section(4, 2, 2), Section(2, 1, 2)]
            


