from initialize import initialize_and_reconstruct, Infeasible
from optimize import optimize
from pivot import make_dictionary, UNBOUNDED
import numpy as np

def simplex(dictionary, basic_vars, non_basic_vars):
    dict_, basic, non_basic = initialize_and_reconstruct(dictionary, basic_vars, np.array(non_basic_vars))
    res, _ = optimize(dict_, basic, non_basic)
    if res == UNBOUNDED:
        raise Infeasible()
    return dict_, basic, non_basic
    
def simplex_optimal_values(dictionary, basic_vars, non_basic_vars):
    return collect_result(*simplex(dictionary, basic_vars, non_basic_vars), original_non_basic = non_basic_vars)
 
def simplex_input(file_path):
    return simplex_optimal_values(*make_dictionary(file_path))

def collect_result(final_dict,final_basic, final_non_basic, original_non_basic):
    optimal_values = []
    for v in original_non_basic:
        if v not in final_basic:
            optimal_values.append(0)
        else:
            optimal_values.append(final_dict[final_basic == v][0, 0])
    return final_dict[-1, 0], set(zip(original_non_basic, optimal_values))

if __name__ == '__main__':
    import sys
    print(simplex_input(sys.argv[1]))

############################## TESTS ##############################
import pytest

def construct_out(input_path):
    with open(input_path + ".out") as f:
        res = float(f.readline())
        optimal_values = set()
        for var, val in map(str.split, f):
            optimal_values.add((int(var), float(val)))
    return res, optimal_values

@pytest.mark.parametrize("i", range(1, 5))
def should_run_simplex_end_to_end(i):
    input_path = 'simplexTests/dict%d' % i
    assert_equals(construct_out(input_path), simplex_input(input_path))

def assert_equals(expected, actual):
    assert expected[0] - actual[0] < 0.0000000001
    expected_vars, actual_vars = dict(expected[1]), dict(actual[1])
    for v in expected_vars.keys():
        assert expected_vars[v] - actual_vars[v] < 0.0000000001
        
    
