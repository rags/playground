from initialize import initialize_and_reconstruct
from optimize import optimize
from pivot import make_dictionary
import numpy as np

def simplex(dictionary, basic_vars, non_basic_vars):
    dict_, basic, non_basic = initialize_and_reconstruct(dictionary, basic_vars, np.array(non_basic_vars))
    optimize(dict_, basic, non_basic)
    return dict_, basic, non_basic

def simplex_optimal_values(dictionary, basic_vars, non_basic_vars):
    dict_, basic, non_basic = simplex(dictionary, basic_vars, non_basic_vars)
    optimal_values = []
    for v in non_basic_vars:
        if v not in basic:
            optimal_values.append(0)
        else:
            optimal_values.append(dict_[basic == v][0, 0])
    return dict_[-1, 0], set(zip(non_basic_vars, optimal_values))

def simplex_input(file_path):
    return simplex_optimal_values(*make_dictionary(file_path))

if __name__ == '__main__':
    import sys
    print(simplex_input(sys.argv[1]))

############################## TESTS ##############################

def construct_out(input_path):
    with open(input_path + ".out") as f:
        res = float(f.readline())
        optimal_values = set()
        for var, val in map(str.split, f):
            optimal_values.add((int(var), float(val)))
    return res, optimal_values
        
def should_run_simplex_end_to_end():
    for i in range(1, 4):
        input_path = 'simplexTests/dict%d' % i
        assert construct_out(input_path) == simplex_input(input_path)
    
