import pivot

def optimize(dictionary, basic_vars, non_basic_vars):
    cnt = 0
    while True:
        res, _ = pivot.pivot(dictionary, basic_vars, non_basic_vars)
        if res != pivot.SUCCESS:
            break
        cnt += 1
    
    return (pivot.UNBOUNDED, cnt) if res == pivot.UNBOUNDED else (dictionary[-1][0], cnt)
        
def optimize_input(file_path):
    with open(file_path) as f:
        return optimize(*pivot.make_dictionary(f))

def optimize_io(file_path):
    res, cnt = optimize_input(file_path)
    with open(file_path + ".out", "w") as out:
        if res is pivot.UNBOUNDED:
            out.write(pivot.UNBOUNDED)
        else:
            out.write("%s\n" % res)
            out.write("%s\n" % cnt)

if __name__ == '__main__':
    import sys
    optimize_io(sys.argv[1])


############################## TESTS ##############################

def should_optimize():
    for i in range(1, 11):
        res, cnt = optimize_input('part2TestCases/unitTests/dict%s' % i)
        with open('part2TestCases/unitTests/dict%s.output' % i) as out:
            if res is pivot.UNBOUNDED:
                assert out.readline().strip() == pivot.UNBOUNDED
            else:
                assert res - float(out.readline()) < .001
                assert int(out.readline()) == cnt
    