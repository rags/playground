import sys

def extend(paths, delta):
    for path in paths:
        yield '\t'.join(path + delta)

def extend_paths(input):
    cur_frontier = None
    delta = None
    paths_to_be_extended = None
    for line in map(str.strip, input):
        frontier, *rest = line.split('\t')
        if frontier != cur_frontier:
            if cur_frontier:
                yield from extend(paths_to_be_extended, delta)
            cur_frontier = frontier
            paths_to_be_extended = []
            delta = []
        if '#' in rest:
            paths_to_be_extended.append(rest)
        else:
            delta = rest
    if cur_frontier:
        yield from extend(paths_to_be_extended, delta)
            

def main():
    for i in extend_paths(sys.stdin):
        print(i)

if __name__ == '__main__':
    main()
        