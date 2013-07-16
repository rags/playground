import numpy as np
'''
substring DP problem
T(N)=T(N-1)+T(N-2)
the solution is between 2T(N-2) and 2T(N-1)
Approx: i.e between 2^N and 2^(n/2) i.e, sqrt(2)^N i.e 1.414^N

Note:
The actual value is O(φ^N)
φ, the golden ratio = (1+sqrt(5))/2= 1.168..

'''
def nchoosek_recur(n, k):
    assert k <= n
    if k == n or k == 0:
        return 1
    return nchoosek_recur(n-1, k) + nchoosek_recur(n - 1, k - 1)

#O(n^2)
#O(n*k) = stricly <= O(n*n/2) because k varies from 0 to n/2 because min(k,n-k)
def nchoosek_dp(n, k):
    k= min(k, n - k) #nCk==nCn-k- so choose smaller k value; optimization
    matrix = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        matrix[i][0] = matrix[i][i] = 1
        for j in range(1, k + 1):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

 #   print matrix
    return matrix[n][k]
    


############################## TESTS ##############################
import pytest

@pytest.mark.parametrize('algorithm', [nchoosek_recur, nchoosek_dp])
def should_nchoosek(algorithm):
    assert 2 == algorithm(2, 1)
    assert 10 == algorithm(5, 2)
    assert 20 == algorithm(6, 3)
    assert 28 == algorithm(8, 6) == algorithm(8, 2)
    
    for n in range(10):#next loop duplicated this assertion
        assert 1 == algorithm(n, 0) == algorithm(n, n)

    for n in range(20):#nCk == nCn-k
        for k in range(n + 1):
            assert algorithm(n, k) == algorithm(n, n - k)
