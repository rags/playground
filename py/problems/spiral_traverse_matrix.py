def traverse(matrix):
    m, n = len(matrix), len(matrix[0])
    ilb,jlb,iub,jub=0,0,m,n
    out=[]
    while True:
        if ilb>=iub or jlb>=jub:
            break
        i = ilb
        for j in range(jlb, jub):
            out.append(matrix[i][j])
        for i in range(ilb + 1,iub):
            out.append(matrix[i][j])
        if iub - 1 > ilb:
            for j in range(jub - 2, jlb - 1, -1):
                out.append(matrix[i][j])
        if jub - 1 > jlb:
            for i in range(iub - 2, ilb, -1):
                out.append(matrix[i][j])
        ilb,jlb,iub,jub=ilb+1,jlb+1,iub-1,jub-1
    return out    

def traverse_complicated_shit(matrix):
    m, n = len(matrix), len(matrix[0])
    #print('\n'.join(map(lambda row: ' '.join(row),x)))
    i,j=0,-1
    ilb,jlb,iub,jub=0,-1,m,n
    out=[]
    while True:
        if ilb>=iub or jlb>=jub:
            break
        j+=1
        while j<jub:
            out.append(matrix[i][j])
            j+=1
        j=jub-1    
        i+=1
        while i<iub:
            out.append(matrix[i][j])
            i+=1
        i=iub-1
        j-=1
        while j>jlb and iub-1>ilb:
            out.append(matrix[i][j])
            j-=1
        j=jlb+1    
        i-=1
        while i>ilb and jub-1>jlb+1:
            out.append(matrix[i][j])
            i-=1
        ilb,jlb,iub,jub=ilb+1,jlb+1,iub-1,jub-1
        i,j=ilb,jlb
        
    return out    


############################## TESTS ##############################
import pytest

def build_matrix(m, n):
    return [[str(i)+str(j) for j in range(n)] for i in range(m)]

    
@pytest.mark.parametrize(('algorithm'), [traverse, traverse_complicated_shit])
@pytest.mark.parametrize(('input', 'output'), [
    (build_matrix(1, 1), ['00']), 
    (build_matrix(2, 2), ['00', '01', '11', '10']), 
    (build_matrix(7, 3), ['00', '01', '02', '12', '22', '32', '42', '52',
                          '62', '61', '60', '50', '40', '30', '20', '10',
                          '11', '21', '31', '41', '51']), 
    (build_matrix(1, 4), ['00', '01', '02', '03']),
    (build_matrix(5, 1), ['00', '10', '20', '30', '40']),
    (build_matrix(6, 7), ['00', '01', '02', '03', '04', '05', '06', '16', '26', '36',
                          '46', '56', '55', '54', '53', '52', '51', '50', '40', '30',
                          '20', '10', '11', '12', '13', '14', '15', '25', '35', '45',
                          '44', '43', '42', '41', '31', '21', '22', '23', '24', '34',
                          '33', '32']),
    (build_matrix(8, 5), ['00', '01', '02', '03', '04', '14', '24', '34', '44', '54',
                          '64', '74', '73', '72', '71', '70', '60', '50', '40', '30',
                          '20', '10', '11', '12', '13', '23', '33', '43', '53', '63',
                          '62', '61', '51', '41', '31', '21', '22', '32', '42', '52'])
])
def should_traverse(input, output, algorithm):
    m, n = len(input), len(input[0])
    assert output == algorithm(input)
    assert len(set(output)) == m * n
    
