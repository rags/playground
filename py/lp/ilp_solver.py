from pivot import make_dictionary
from simplex import simplex
import numpy as np
from math import floor

def solve_ilp_input(file_path):
    dictionary, basic_vars, non_basic_vars = make_dictionary(file_path)
    cur_dict, cur_basic, cur_non_basic = simplex(
            dictionary, basic_vars, non_basic_vars)
    print(cur_dict)    
    while True:
        if all_objective_vars_are_int(cur_dict, cur_basic, non_basic_vars):
            return cur_dict, cur_basic, cur_non_basic
        fractional_eqns=cur_dict[np.array(
            np.floor(cur_dict[:,0]).H!=cur_dict[:,0].H)[0]]
        cutting_planes = fractional_eqns - np.floor(fractional_eqns)
        cutting_planes[:, 0] = -cutting_planes[:, 0]
        cur_dict = np.vstack(cur_dict, cutting_planes)
        cur_max_var =  max(np.r_[cur_non_basic, cur_basic])
        cur_basic = np.r_[cur_basic, range(cur_max_var + 1, cur_max_var + 1 + len(cutting_planes))]

def all_objective_vars_are_int(dictionary, basic_vars, objective):
    for v in objective:
        found = basic_vars == v
        if any(found)  and dictionary[found, 0] - floor(dictionary[found, 0]) > 0.0000000000001:
            return False
    return True
    
if __name__ == '__main__':
    import sys
    solve_ilp_input(sys.arvg[1])

############################## TESTS ##############################
import pytest

@pytest.mark.parametrize("i", [7])#range(1, 11))
def should_solve_ilp(i):
    input_file = "ilpTests/unitTests/ilpTest%d" % i
    dict_, _, _ = solve_ilp_input(input_file)
    with open(input_file + ".output") as f:
        expected = float(f.readline())
        assert dict_[-1,0] - expected < 0.0000000000001, "%s e=%s a=%s" % (input_file, expected, dict_[-1, 0])