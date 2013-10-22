import sys


def combs(links):
    for i in range(1, len(links)):
        links[0], links[i] = links[i], links[0]
        yield '\t'.join(links)
    
def format_connections(network):
    for line in map(str.strip, network):
        user, *network= line.split('\t')
        #user, network = line.split('\t')[0], line.split('\t')[1:] #2.7.x
        network.sort()
        if '#' in network:
            network.remove('#')
        yield user + '\t' + '\t'.join(network)

def main():
    for formatted in format_connections(sys.stdin):
        print(formatted)

if __name__ == '__main__':
    main()
        