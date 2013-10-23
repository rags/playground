import sys

def combs(links, n=None):
    n = n or len(links)
    for i in range(1, n):
        links[0], links[i] = links[i], links[0]
        yield '\t'.join(links)
    
def link_combinations(network):
    for line in map(str.strip, network):
        yield line
        links = line.split('\t')
        if '#' not in links: #no network beyond immediate friends
            yield from combs(links)
            #for comb in combs(links): yield comb #py 2.7
        else:
            n = links.index('#')
            links.remove('#')
            for comb in combs(links, n):
                yield comb.replace('\t', '\t#\t', 1)

def main():
    for combination in link_combinations(sys.stdin):
        print(combination)

if __name__ == '__main__':
    main()
        