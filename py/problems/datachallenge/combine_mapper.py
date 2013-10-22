import sys
    
def combine(network):
    for line in map(str.strip, network):
        if '#' in line:
            _, *network= line.split('\t')
            #user, network = line.split('\t')[0], line.split('\t')[1:] #2.7.x
            network.remove('#')
            for connection in network:
                yield connection + '\t' + line
        else:
            yield line

def main():
    for i in combine(sys.stdin):
        print(i)

if __name__ == '__main__':
    main()
        