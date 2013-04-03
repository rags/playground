def color(graph):
    uncolored_nodes = graph.keys()
    color = 0
    colors = {node: None for node in uncolored_nodes}
    #for i in xrange(len(uncolored_nodes)):
    while(uncolored_nodes):
        color += 1
        nodes = []
        for node in uncolored_nodes:
            if all([colors[neighbor] != color for neighbor in graph[node]]):
                colors[node] = color
            else:
                nodes.append(node)
        print colors
        uncolored_nodes = nodes

    return color, colors

def is_valid(graph, colors):
    for node in graph:
        for neighbor in graph[node]:
            if not colors[node]:
                print "Node %s not colored" % node
                return 
            if colors[node] == colors[neighbor]:
                print "Nodes %s,%s have same color %s" % (node, neighbor, colors[node])
                return
    return True
    
############################## TESTS ##############################
    
SOUTH_INDIA = {'KA': ['MH', 'AP', 'TN', 'KL', 'GA'], 
               'KL': ['TN', 'KA'], 
               'TN': ['KL', 'KA', 'AP'],
               'AP': ['KA', 'TN', 'MH', 'OR', 'CG'],
               'GA': ['KA', 'MH'], 
               'MH': ['KA', 'AP', 'GA', 'GJ', 'MP', 'CG'], 
               'MP': ['MH', 'CG', 'GJ'],
               'GJ': ['MH', 'MP'], 
               'CG': ['OR', 'MP', 'MH', 'AP'], 
               'OR': ['AP', 'CG']
}

'''
                               
                            __(A)__ 
                         __/   |   \__
                      __/      |      \__
                   __/         |         \__
                __/            |             \__
             __/              (C)              \__
          __/                /   \                \__
       __/                   |   |                   \__ 
    (B)___                  /     \                  ___(D)
     |     \__               |     |               __/    /
     \      (E)------------/-------\------------(F)      /
      |       \_           |       |           _/       |
      \         \_        /         \        _/        /
       |          \_      |         |      _/          |
       \            \__  /           \  __/           /
        |              \_|           |_/              |
        \               /\_         _/\              /
         |              |  \_     _/  |              |
         \             /     \___/     \            /
          |            |     _/ \_     |            |
          \           /    _/     \_    \          /
           |          |  _/         \_  |          |
           \          |_/             \_|          / 
            |       (G)                 (H)       | 
            \     _/                       \_    /
             |   /                           \   |
              \ /                             \ /
               (I)----------------------------(J)
                                              
    
'''
PETERSEN = {'A': ['B', 'C', 'D'],
            'B': ['A', 'E', 'I'],
            'C': ['A', 'G', 'H'], 
            'D': ['A', 'F', 'J'],
            'E': ['B', 'F', 'H'],
            'F': ['D', 'E', 'G'],
            'G': ['C', 'F', 'I'],
            'H': ['C', 'E', 'J'],
            'I': ['B', 'G', 'J'],
            'J': ['D', 'H', 'I']}

BIPATITE = {'A': [1, 2, 3], 
            'B': [1, 2, 3], 
            'C': [1, 2, 3], 
            1: ['A', 'B', 'C'], 
            2: ['A', 'B', 'C'], 
            3: ['A', 'B', 'C']}

def should_color_south_and_central_india():
    color_cnt, colors = color(SOUTH_INDIA)
    assert 4 == color_cnt
    assert is_valid(SOUTH_INDIA, colors)

    color_cnt, colors = color(PETERSEN)
    assert 3 == color_cnt
    assert is_valid(PETERSEN, colors)

    color_cnt, colors = color(BIPATITE)
    assert 2 == color_cnt
    assert is_valid(BIPATITE, colors)
    assert colors['A'] == colors['B'] == colors['C']
    assert colors[1] == colors[2] == colors[3]

    
