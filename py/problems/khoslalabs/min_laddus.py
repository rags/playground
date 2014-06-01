'''
Lakshmi is a primary school teacher. She wants to give some laddus to the children in her class. All the students sit in a line and each of them has a rating score according to his or her usual performance. Lakshmi wants to give at least 1 laddu for each child. Children get jealous of their immediate neighbors, so if two children sit next to each other then the one with the higher rating must get more laddus. Lakshmi wants to save money, so she wants to minimize the total number of laddus.

Tip: Please understand the question clearly and pay good attention to below provide - sample input and output - completely in order to arrive at correct solution.

Input

The first line of the input is an integer N, the number of children in Lakshmi's class. Each of the following N lines contains an integer indicates the rating of each child.

Ouput

Output a single line containing the minimum number of laddus Lakshmi must give.
Explanation
Sample Input

3
1
2
2

Sample Ouput

4

Explanation

The number of laddus Lakshmi must give are 1, 2 and 1.

'''
import sys
if sys.version.startswith("3."):
    raw_input = input


def main():
    n = int(raw_input())
    grades = [float(raw_input()) for i in range(n)]
    print(int(sum(min_laddus(grades))))
    
#O(n)
def min_laddus(grades):
    n = len(grades)
    laddus = [1 for i in range(n)]
    for i in range(1, n):
        if grades[i - 1] < grades[i]:
            laddus[i] = laddus[i - 1] + 1
    for i in range(n - 2,-1,-1):
        if grades[i + 1] < grades[i] and laddus[i] <= laddus[i + 1]:
            laddus[i] = laddus[i + 1] + 1
    return laddus
            
        
if __name__ == '__main__':
	main()


############################## TESTS ##############################

def should_distribute_laddus():
    assert min_laddus([1, 2, 2, 2, 2]) == [1, 2, 1, 1, 1]
    assert min_laddus([1, 2, 3, 1]) == [1, 2, 3, 1]
    assert min_laddus([3, 2, 1]) == [3, 2, 1]
    assert min_laddus([2, 2, 1, 2]) == [1, 2, 1, 2]
    assert min_laddus([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert min_laddus([1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1]
    assert min_laddus([2, 1, 3, 1, 2]) == [2, 1, 2, 1, 2]
    
