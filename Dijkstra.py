#create a graph in list format. Each element is a list of lists. The element index indicate the node identity/number/ 
#the element is of the format [[node(x), length(x)]]

g = [[] for x in range(201)] #note that g[0] is useless

with open('Djikstra.txt', 'r') as f:
    for line in f.readlines():
        data = line.split()
        node = int(data[0])
        for i in range(1, len(data)):
            n, l = data[i].split(',')
            g[node].append([int(n),int(l)])




s = 1
# def NaiveDjikstra(g,s):
x = [s] #store processed verticies
v = [float('inf') for i in range(201)] #store min dist for each vertex
path = ['' for i in range(201)] #store path for each vertex
path[1] = str(s)
v[1] = 0

while True:
    dist = {} #path -> distance
    for node in x:
        for nei, distance in g[node]:
            if nei in x:
                continue
            route = path[node]+' '+str(nei)
            dist[route] = v[node] + distance
                
    mindist = min(dist.values())
    
    for key, val in dist.items():
        if val == mindist:
            endnode = int(key.split(' ')[-1])
            v[endnode] = val
            path[endnode] = key
            x.append(endnode)
            break
    
    if len(x) == 200:
        break


    
            
    


