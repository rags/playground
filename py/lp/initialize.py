import pivot
import optimize
import numpy as np

class Infeasible(Exception):
    pass

THRESHOLD = 0.000001

def initialize(dictionary, basic_vars, non_basic_vars):
    m, n = np.shape(dictionary)
    has_neg = any(dictionary[:-1, 0] < 0)
    if not has_neg:
        return dictionary, basic_vars, non_basic_vars, False
    init_dict = np.vstack((np.c_[dictionary[:-1], np.ones((m - 1, 1))], np.r_[np.zeros(n), -1]))
    init_non_basic_vars =  np.r_[non_basic_vars, 0]
    init_basic_vars = np.array(basic_vars)
    entering, leaving = (len(init_non_basic_vars),
                         min(range(m - 1), key = lambda i: init_dict[i, 0]))

    pivot.pivot_for(init_dict, init_basic_vars,
                    init_non_basic_vars, entering, leaving)
    optimize.optimize(init_dict, init_basic_vars, init_non_basic_vars)
    return init_dict, init_basic_vars,  init_non_basic_vars, True

def initialize_and_reconstruct(dictionary, basic_vars, non_basic_vars):
    new_dict, new_basic_vars, new_non_basic_vars, initialized = initialize(dictionary,
                                                                           basic_vars,
                                                                           non_basic_vars)

    if not initialized:
        if not np.any(new_dict[-1, 1:] > 0):
            raise Infeasible()
        return dictionary, basic_vars, non_basic_vars
    if abs(new_dict[-1, 0]) > THRESHOLD or 0 not in new_non_basic_vars:
        print (new_dict)
        raise Infeasible()

    exclude_aux_var = new_non_basic_vars != 0
    new_dict = new_dict[:-1, np.r_[True, exclude_aux_var]]
    new_non_basic_vars = new_non_basic_vars[exclude_aux_var]
    objective = dictionary[-1,1:]
    new_objective_row = np.zeros((1, len(non_basic_vars) + 1))
    for i, v in enumerate(non_basic_vars):
        if v in new_non_basic_vars:
            new_objective_row[0, i + 1] += objective[0, i]
        else:
            new_objective_row += objective[0, i] * new_dict[new_basic_vars == v] 
    return np.vstack((new_dict, new_objective_row)), new_basic_vars, new_non_basic_vars
    

def initialize_input(file_path):
    dictionary, basic_vars, non_basic_vars = pivot.make_dictionary(file_path)
    return initialize(dictionary, basic_vars, non_basic_vars)

def initialize_io(file_path):
    dict_, _, _, _= initialize_input(file_path)
    with open(file_path + ".out", "w") as out:
            out.write("%s\n" % dict_[-1, 0])

if __name__ == '__main__':
    import sys
    initialize_io(sys.argv[1])

############################## TESTS ##############################
import glob

def should_not_initialize_neg_zero():
    _, _, _, initialized = initialize(np.mat('1 2 3;-0.0 1 2;-0.0 3 4'), None, None)
    assert not initialized
    

def should_initialize():
    for i in range(1, 11):
        dict_, _, _, _= initialize_input('initializationTests/unitTests/idict%s' % i)
        print (i, dict_)
        with open('initializationTests/unitTests/idict%s.out' % i) as out:
            assert abs(dict_[-1, 0] - float(out.readline())) < 0.001
    for path in glob.iglob("initializationTests/unitTests/moreTests/*.dict"):
        dict_, _, _, _= initialize_input(path)
        with open(path + ".out") as out:
            assert abs(dict_[-1, 0] - float(out.readline())) < 0.001


def should_initialize_and_reconstuct():
    with open('simplexTests/dict1') as inp, open('simplexTests/dict1.initialized') as out: 
        dictionary, basic_vars, non_basic_vars = initialize_and_reconstruct(*pivot.make_dictionary(inp))
        expected_dict, expected_basic, expected_non_basic = pivot.make_dictionary(out)
        assert set(basic_vars) == set(expected_basic)
        assert set(non_basic_vars) == set(expected_non_basic)
        assert all(abs(dictionary[:, 0] - expected_dict[:, 0]) < 0.0001)
        print(dictionary, non_basic_vars)
        print(expected_dict, expected_non_basic)
        for v in non_basic_vars:
            col = dictionary[:, np.r_[False, non_basic_vars == v]]
            expected_col = expected_dict[:, np.r_[False, expected_non_basic == v]]
            for bv in basic_vars:
                print (col[bv == basic_vars], expected_col[bv == expected_basic])
                assert all(abs(col[bv == basic_vars] - expected_col[bv == expected_basic]) < 0.0001)
            assert all(abs(col[len(basic_vars)] - expected_col[len(basic_vars)]) < 0.0001)
                
