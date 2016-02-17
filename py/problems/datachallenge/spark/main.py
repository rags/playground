import sys, math
import os.path as path
from pyspark import SparkContext

def read(sc, file):
    return  sc.textFile(file)
        
def build_network(line):
    key, *links = line.split()
    network = {key: set(links)}    
    yield key, network
    for link in links:
        yield link, network
    if len(links) == 1:
        reverse_network = {links[0]: {key}}
        yield links[0], reverse_network
        yield key, reverse_network

def union(network1, network2):
    for k in network2:
        if k in network1:
            network1[k].update(network2[k])
        else:
            network1[k] = network2[k]
    return network1

def combine(network, delta):
    for k, v in delta.items():
        for nk, nv in network.items():
            v.update(nv)
            nv.update(v)
            if k in v:
                v.remove(k)
            if nk in nv:
                nv.remove(nk)    
        if k not in network:
            network[k] = v
    print("====")
    print(network)
    return network

def flatten_network(tup):
    for k, v in tup[1].items():
        yield k, v
        
def expand_network(network):
    print(network.flatMap(build_network).filter(lambda tup: tup[0] == 'torsten') 
          .aggregateByKey({}, combine, union).collect())
    print("-------------")
    
    return network.flatMap(build_network) \
                  .aggregateByKey({}, combine, union) \
                  .flatMap(flatten_network) \
                  .aggregateByKey(set(), set.union, set.union)
    

'''
1 <--> 2 <--> 3 <--> 4 <--> 5 <--> 6 <--> 7 <--> 8
extension n3+ n2 = n5
n3:
1 2 3 4
2 3 4 5 1
3 4 5 6 1 2
4 5 6 7 1 2 3
5 6 7 8 4 3 2
6 7 8 5 4 3
7 8 6 7 5 4
8 7 6 5

n2:
1 2 3 
2 3 4 1
3 4 5 2 1
4 5 6 3 2
5 6 7 4 3
6 7 8 5 4
7 8 6 5
8 7 6

n5:
1 2 3 4 5 6
2 3 4 5 6 7 1
3 4 5 6 7 8 1 2
4 5 6 7 8 3 2 1
5 6 7 8 4 3 2 1
6 7 8 5 4 3 2 1
7 8 6 5 4 3 2 
8 7 6 5 4 3

'''
    

def extension_mapper(connections):
    for key, links in connections:
        network = {key: links}
        yield key, network
        if len(links) == 1:
            reverse_network = {links[0]: {key}}
            yield links[0], network
            yield links[0], reverse_network
            yield key, reverse_network

def extend_links(join):
    (frontier, (cur_frontier, extension)) = join
    for k, v in cur_frontier:
        v.update(next(iter(extension.values())))
        if k in v:
            v.remove(k)
        yield k, v
            
def extend(cur_frontier, extension):
    return cur_frontier.flatMap(build_network) \
                       .join(extension.flatMap(extension_mapper)) \
                       .map(extend_links) \
                       .aggregateByKey(set(), set.union, set.union)
    
def deg_of_separation(seed, degree, sc):
    rdds = {1: read(sc, seed)}
    highest_pow2 = math.floor(math.log2(degree))
    for i in range(1, highest_pow2 + 1):
        deg = 2 ** i
        rdds[deg] = expand_network(rdds[deg // 2]) 

    network = rdds[2 ** highest_pow2]
    for i in range(highest_pow2 - 1, -1, -1):
        deg =  2 ** i
        if deg & degree:
            network = extend(network, rdds[2 ** i])
    return network
            
def main():
    l =  len(sys.argv)
    if l < 2:
        print('Usage: main.py', file = sys.stderr)
        exit(-1)
    sc =  SparkContext(appName='Network')
    # out =  deg_of_separation(sys.argv[1], (2 if l < 3 else int(sys.argv[2])), sc) \
    #     .map(lambda rec:rec[0] + " " + " ".join(rec[1]))
    # print(out.collect())
    #lines =  read(sc, sys.argv[1:2])
    expand_network(read(sc, sys.argv[1]))

    #
    #expand_network(lines).map(lambda rec:rec[0] + "\t" + "\t".join(rec[1])).saveAsTextFile("out/ffff")
    sc.stop()

    
if __name__ ==  '__main__':
    main()
