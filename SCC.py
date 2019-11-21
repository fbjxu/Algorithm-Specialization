import collections
filename = 'SCC.txt'
#read txt file to a graph, using list of lists
g = [[] for x in range(875715)] #first one element is useless
grev = [[] for x in range(875715)]

with open(filename,'r') as f:
    for line in f.readlines():
        key, val = line.split()
        g[int(key)].append(int(val))
        grev[int(val)].append(int(key))


v = [0 for i in range(875715)]
t = []
#also assign a f(v) to each node
#use stack implementing dfs

#fill order
for i in range(1,len(grev)):
    order = []
    if v[i] == 0:
        stack = []
        stack.append(i)
        v[i] = 1

    while len(stack) > 0:
        node = stack.pop()
        order.append(node)

        for nei in grev[node]:
            if v[nei] == 0:
                stack.append(nei)
                v[nei] = 1
    #fill t using order
    for e in range(len(order)-1, -1, -1):
        t.append(order[e])



#need to use g from now on

leader = []
vi = [0 for i in range(875715)]
#traverse g using t (traverse t in reverse)
for f in t[::-1]:
    if vi[f] == 0:
        staq = []
        leader.append(f)
        staq.append(f)
        vi[f] = 1
    
    while len(staq) > 0:
        node = staq.pop()
        for nei in g[node]:
            if vi[nei] == 0:
                staq.append(nei)
                vi[nei] = 1
    








