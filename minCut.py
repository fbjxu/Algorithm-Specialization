from random import choice
import copy

mygraph = {}
with open ('MinCut.txt', 'r') as file:
    for f in file.readlines():
        v = (f.split())
        mygraph[v[0]] = v[1:]


def minCuthelper(g):
    #pink a random edge
    #first pick random vetex:
    while len(g) > 2:
        vertex =  choice(list(g.keys())) #string
        edge = [vertex, choice(list(g[vertex]))] #list of 2 strings
        a, b = edge[0], edge[1]
        #after picking the edge, fuse the corresponding two points
        try:
            #fuse points
            #step 1: let points previously connected to b be connected to a
            for n in g[b]:
                g[n].remove(b)
                g[n].append(a)
            #step 2: add b connections to a
            g[a].extend(g[b])

            #step 3: remove self-looping edges
            while a in g[a]:
                g[a].remove(a)
            #step 4: everything is good, remove b from graph
            del(g[b])

        except KeyError:
            print('Index error for removing edges')
    #result checking
    # print(list(g.items())[1])
    # print(len(list(g.items())[0][1]))
    return len(list(g.items())[0][1])



def mincut(graph, trials):
    result = []
    for i in range(trials):
        g = copy.deepcopy(graph)
        result.append(minCuthelper(g))
    
    return result

final_result = mincut(mygraph, 300)
