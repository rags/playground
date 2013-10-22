import sys

def consolidate(connections):
    cur_user = None
    friends = None
    extended_friends = None

    #format: user friends # nth_deg_network
    def construct_ouput():
        friendstr = '\t'.join(friends)
        extended_friendstr = '\t'.join(extended_friends - friends)
        return (cur_user + (('\t' + friendstr) if friendstr else '') 
                + '\t#' + (('\t' + extended_friendstr) if extended_friends else ''))
        
    for connection in map(str.strip, connections):
        user, *network = connection.split('\t') #3.x
        #user, network = friends.split('\t')[0],friends.split('\t')[1:] #2.7.x
        if user != cur_user or cur_user is None:
            if cur_user:
                yield construct_ouput()
            cur_user = user
            friends = set()
            extended_friends = set()
        if '#' in network:
            i =  network.index('#')
            friends.update(network[:i])
            extended_friends.update(network[i + 1:])
        else:
            friends.update(network)
    if cur_user:
        yield construct_ouput()

def main():
    for user_network in consolidate(sys.stdin):
        print(user_network)

        
if __name__ == '__main__':
    main()

            