def find_max_across(a,low,mid,high):
    left_sum=cursum=a[mid-1]
    left_low=mid-1
    for i in range(mid-2,low-1,-1):
        cursum += a[i]
        if(cursum > left_sum): 
            left_low = i 
            left_sum = cursum
        
    cursum = right_sum = a[mid]
    right_high=mid+1
    for i in range(mid+1,high):
        cursum += a[i]
        if(cursum > right_sum): 
            right_sum = cursum
            right_high = i+1 
    return (left_low,right_high,left_sum + right_sum)
        
    
def find_max_subarray(a,low,high):
    if(low >= len(a)):
        return (-1,-1,0)
    if(high==low+1 or high==low):
        return (low,high,a[low])
    mid = (low + high)//2
    result = left = find_max_subarray(a,low,mid)
    right = find_max_subarray(a,mid+1,high)
    if(right[2]>result[2]): 
        result = right
    across = find_max_across(a,low,mid,high)
    if(across[2]>result[2]): 
        result = across
    return result


def max_subarray(a):
    low,high,sum = find_max_subarray(a,0,len(a))
    return a[low:high]

def max_subarray_kadane(a):
    max_ending_here = max_so_far = 0
    max_arr_ending_here, max_arr_so_far = [], []
    for x in a:
        if max_ending_here + x >= 0:
            max_ending_here = max_ending_here + x
            max_arr_ending_here.append(x)
        else:
            max_ending_here = 0
            max_arr_ending_here = []
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_arr_so_far = max_arr_ending_here[:]
    return max_arr_so_far

############################## TESTS ##############################

import pytest

def main():
    #print max_subarray([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])
    #print max_subarray([13,18,20,-7,12,-3,-25,20,-3,-16,-23,-5,-22,15,-4,7])
    #print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])                     
    print max_subarray([13,18,20,-7,7,-3,-25,20,-3,-16,-23,-5,-22,15,-4,7])


@pytest.mark.parametrize('algorithm', [max_subarray, max_subarray_kadane])
def should_find_max_subarray(algorithm):
    assert algorithm([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7])==[18,20,-7,12]
    assert algorithm([13,18,20,-7,12,-3,-25,20,-3,-16,-23,-5,-22,15,-4,7])==[13,18,20,-7,12]
    assert algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4])==[4,-1,2,1]
    assert algorithm([13,18,20,-7,7,-3,-25,20,-3,-16,-23,-5,-22,15,-4,7])==[13,18,20]
    assert algorithm([-7,-3,-2,-10,-6,-50])==[]
    assert algorithm([-7,-3,-2,-10,-6,-1])==[]

if __name__=="__main__":
    main()
