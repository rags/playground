import numpy as np
from simplex import simplex as simplexfunc
from optimize import optimize as optimizefunc

'I love numpy thats 10 classes of java code in one line'
def dual(dictionary):
    return -np.vstack((np.c_[dictionary[-1,1:].H,dictionary[:-1,1:].H],
                       np.c_[dictionary[-1,0],dictionary[:-1,0].H]))


def simplex(dictionary, basic_vars, non_basic_vars):
    final_dict, basic, non_basic = simplexfunc(dual(dictionary), non_basic_vars, basic_vars)
    return dual(final_dict), non_basic, basic


def optimize(dictionary, basic_vars, non_basic_vars):
    dict_ = dual(dictionary)
    status, optimal_value = optimizefunc(dict_, non_basic_vars, basic_vars)
    return dual(dict_), basic_vars, non_basic_vars


############################## TESTS ##############################
from pytest import fixture

@fixture
def dictionary():
    return np.mat('''4.33333333333       0.333333     0.666667      -0.333333;
                        8.66666666667    -0.333333    0.333333      -2.66666666667;
                        10               0            0             -1;
                        3                -3           1             -18;
                        5.66666666667    -0.333333    -0.6666666667 0.333333;
                        1.333333         0.333333     -0.333333     2.6666666667;
                        -0.333333        0.6666666667 0.333333      0.333333;    
                        -0.6666666667    0.333333     0.6666666667  0.6666666667;
                        -0.6666666667    0.333333     0.6666666667  0.6666666667;
                        -0.333333        0.6666666667 0.333333      0.333333;    
                        7                0             -1            -2''')
    
def should_dualize(dictionary):
    dual_ = dual(dictionary)
    assert np.all(dictionary[:-1,1:].H == -dual_[:-1,1:])
    assert dictionary[-1,0] == -dual_[-1,0]
    assert np.all(dictionary[-1,1:].H == -dual_[:-1,0])
    assert np.all(dictionary[:-1,0].H == -dual_[-1,1:])
    assert np.all(dictionary==dual(dual_))


def should_optimize(dictionary):
    sim_dict, sim_basic, sim_non_basic = simplex(dictionary, np.array([4, 5, 6, 7, 1, 2, 10, 11, 12, 13]), np.array([8, 9, 3]))
    opt_dict, opt_basic, opt_non_basic = optimize(dictionary, np.array([4, 5, 6, 7, 1, 2, 10, 11, 12, 13]), np.array([8, 9, 3]))
    assert np.all(opt_dict == sim_dict)
    assert np.all(opt_basic == sim_basic)
    assert np.all(opt_non_basic == sim_non_basic)
    assert np.all(sim_non_basic == np.array([11, 7, 3]))
    assert np.all(sim_basic == np.array([4, 5, 6, 9, 1, 2, 8, 10, 12, 13]))
    assert abs(6.57142857143 - sim_dict[-1, 0]) <= 0.0001 and  abs(6.57142857143 - opt_dict[-1, 0]) < 0.0001

