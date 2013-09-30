import pivot
import optimize
def initialize(dictionary, basic_vars, non_basic_vars):
    has_neg = any(map(lambda row: row[0] < 0, dictionary))
    if not has_neg:
        return dictionary
    init_dict = dictionary[:-1]
    for row in init_dict:
        row.append(1)
    init_dict.append([0] * (len(non_basic_vars) + 1) + [-1])
    init_non_basic_vars =  non_basic_vars +  [0]
    entering, leaving = (len(init_non_basic_vars),
                         min(range(len(dictionary) - 1), key = lambda i: dictionary[i][0]))
    pivot.pivot_for(init_dict, basic_vars,
                    init_non_basic_vars, entering, leaving)
    optimize.optimize(init_dict, basic_vars, init_non_basic_vars)
    return init_dict

def initialize_input(file_path):
    with open(file_path) as f:
        dictionary, basic_vars, non_basic_vars = pivot.make_dictionary(f)
    return initialize(dictionary, basic_vars, non_basic_vars)

def initialize_io(file_path):
    dict_ = initialize_input(file_path)
    with open(file_path + ".out", "w") as out:
            out.write("%s\n" % dict_[-1][0])

if __name__ == '__main__':
    import sys
    initialize_io(sys.argv[1])

############################## TESTS ##############################
import glob

def should_initialize():
    for i in range(1, 11):
        dict_ = initialize_input('initializationTests/unitTests/idict%s' % i)
        with open('initializationTests/unitTests/idict%s.out' % i) as out:
            assert abs(dict_[-1][0] - float(out.readline())) < 0.001
    for path in glob.iglob("initializationTests/unitTests/moreTests/*.dict"):
        print(path)
        dict_ = initialize_input(path)
        with open(path + ".out") as out:
            assert abs(dict_[-1][0] - float(out.readline())) < 0.001


    