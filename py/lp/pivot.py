from __future__ import division
SUCCESS, UNBOUNDED, INFEASIBLE = 'SUCCESS', 'UNBOUNDED', 'INFEASIBLE'
import numpy as np
'''
dictionary is (m+1)*(n+1) matrix
dict = c1 + a11X1 + a12X2 + a13X3 .... a1nXn
       c2 + a21X1 + a22X2 + a23X3 .... a2nXn
       .
       .
       cm + a21X1 + a22X2 + a23X3 .... amnXn
      ----------------------------------------
       z  + c1X1  +  c2X2 + c3X3  ....  cnXn
'''
def pivot(dictionary, basic_vars, objective_vars):
    m, n = np.shape(dictionary)
    entering_candidates = [i for i in range(1, n) if dictionary[-1, i] > 0]
    if not entering_candidates:
        return INFEASIBLE, None
    entering = min(entering_candidates, key = lambda i: objective_vars[i - 1])
    leaving_candidates, min_ratio = None, None
    for i in range(0, m - 1):
        cur_entering_coeff = dictionary[i, entering]
        if cur_entering_coeff < 0:
            ratio = dictionary[i, 0] / cur_entering_coeff
            
            if min_ratio is None or  ratio > min_ratio:
                leaving_candidates = [i]
                min_ratio = ratio
            elif ratio == min_ratio:
                leaving_candidates.append(i)

    if not leaving_candidates:
        return UNBOUNDED, None
    leaving = min(leaving_candidates, key = lambda i: basic_vars[i])
    return pivot_for(dictionary, basic_vars, objective_vars, entering, leaving)

def pivot_for(dictionary, basic_vars, objective_vars, entering, leaving):
    m, n = np.shape(dictionary)
    leaving_row = dictionary[leaving]
    leaving_coeff = leaving_row[0, entering]
    for i in range(0, n):
        if i == entering:
            leaving_row[0, i] = 1 / leaving_coeff
        else:
            leaving_row[0, i] /= -leaving_coeff
    for i, coeffs in enumerate(dictionary):
        if i != leaving:
            entering_coeff = coeffs[0, entering]
            for j in range(n):
                if j == entering:
                    coeffs[0, j] = entering_coeff * leaving_row[0, j]
                else:
                    coeffs[0, j] += entering_coeff * leaving_row[0, j]
    (basic_vars[leaving], objective_vars[entering - 1]
     ) =  objective_vars[entering - 1], basic_vars[leaving]
    return SUCCESS, (basic_vars[leaving], objective_vars[entering - 1])
    
def make_dictionary(file):
    if isinstance(file, str):
        with open(file) as f:
            return _make_dictionary(f)
    return _make_dictionary(file)
    
def _make_dictionary(file):
    m, n = map(int, file.readline().split())
    basic_vars = np.array(np.mat(file.readline(), dtype = int))[0]
    objective_vars = np.array(np.mat(file.readline(), dtype = int))[0]
    b_coeffs = np.mat(file.readline())
    dictionary = np.vstack(np.mat(file.readline()) for i in range(m))
    dictionary = np.vstack((np.c_[b_coeffs.H, dictionary], np.mat(file.readline())))
    return dictionary.astype(float), basic_vars, objective_vars

def pivot_once(file_path):
    with open(file_path) as f:
        dictionary, basic_vars, objective_vars = make_dictionary(f)
    res, vars_ = pivot(dictionary, basic_vars, objective_vars)
    with open(file_path + ".out", "w") as f:
        if res == SUCCESS:
            entering, leaving = vars_
            f.write("%s\n" % entering)
            f.write("%s\n" % leaving)
            f.write("%s\n" % dictionary[-1, 0])
        else:
            f.write(res)

if __name__ == '__main__':
    import sys
    pivot_once(sys.argv[1])




############################## TESTS ##############################
def should_pivot_once():
    for i in range(1, 11):
        with open("./part1TestCases/unitTests/dict%s" %  i) as input:
            dictionary, basic_vars, objective_vars = make_dictionary(input)
            res, vars_ = pivot(dictionary, basic_vars, objective_vars)
        with open("./part1TestCases/unitTests/dict%s.output" %  i) as output:

            if res != SUCCESS:
                assert res == output.read().strip()
            else:
                assert vars_ == tuple(map(int, [output.readline(), output.readline()]))
                expected_res = float(output.readline())
                assert abs(expected_res - dictionary[-1, 0]) < .001
