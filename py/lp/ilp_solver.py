from pivot import make_dictionary
from simplex import simplex
import numpy as np
from dual import optimize as dual_simplex, dual
from initialize import Infeasible, THRESHOLD


def solve_ilp_input(file_path):
    dictionary, basic_vars, non_basic_vars = make_dictionary(file_path)
    cur_dict, cur_basic, cur_non_basic = simplex(
            dictionary, basic_vars, non_basic_vars)
    #i = 0
    while True:
        if all_objective_vars_are_int(cur_dict, cur_basic, non_basic_vars):
            return cur_dict, cur_basic, cur_non_basic
        #i += 1
        print("B", cur_dict[ - 1, 0])
        #if i > 10:
        #    break
        fractional_eqns=cur_dict[:-1][np.array(
             cur_dict[:-1,0].H - np.floor(cur_dict[:-1,0]).H > THRESHOLD)[0]]
        print(len(fractional_eqns))
        cutting_planes = np.c_[ -fractional_eqns[:,0] + np.floor(fractional_eqns[:,0]), -fractional_eqns[:,1:] - np.floor(-fractional_eqns[:,1:])]
        cur_dict = np.vstack((cur_dict[:-1], cutting_planes, cur_dict[-1]))
        cur_max_var =  max(np.r_[cur_non_basic, cur_basic])
        cur_basic = np.r_[cur_basic, range(cur_max_var + 1, cur_max_var + 1 + len(cutting_planes))].astype(int)
        print("A", dual(cur_dict))
        cur_dict, cur_basic, cur_non_basic = dual_simplex(cur_dict, cur_basic, cur_non_basic)

def all_objective_vars_are_int(dictionary, basic_vars, objective):
    print(objective, basic_vars)
    for v in objective:
        found = basic_vars == v
        print(np.any(found), v, np.all(np.ceil(dictionary[found, 0]) - dictionary[found, 0] > THRESHOLD), np.all(dictionary[found, 0] - np.floor(dictionary[found, 0]) > THRESHOLD), dictionary[found, 0])
        if (np.any(found) and
            np.all(np.ceil(dictionary[found, 0]) - dictionary[found, 0] > THRESHOLD) and
            np.all(dictionary[found, 0] - np.floor(dictionary[found, 0]) > THRESHOLD)):
            print(float(dictionary[found, 0]).is_integer(), np.ceil(dictionary[found, 0]) - dictionary[found, 0])
            return False
    return True

def solve_ilp_io(file_path):
    try:
        dict_, _, _ = solve_ilp_input(file_path)
        res = str(dict_[-1,0])
    except Infeasible:
        res = "infeasible"
    with open(file_path + ".out", 'w') as f:
        f.write(res)
if __name__ == '__main__':
    import sys
    print(solve_ilp_input(sys.argv[1]))

############################## TESTS ##############################
import pytest

@pytest.mark.parametrize("i", range(1, 10))
def should_solve_ilp(i):
    input_file = "ilpTests/unitTests/ilpTest%d" % i
    with open(input_file + ".output") as f:
        try:
            dict_, _, _ = solve_ilp_input(input_file)
            expected = float(f.readline().strip())
            assert dict_[-1,0] - expected < THRESHOLD
            #, "%s e=%s a=%s" % (input_file, expected, dict_[-1, 0])
        except Infeasible:
            assert f.readline().strip() == "infeasible"

