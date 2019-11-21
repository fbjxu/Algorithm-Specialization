#create a graph in list format. Each element is a list of lists. The element index indicate the node identity/number/ 
#the element is of the format [[node(x), length(x)], [node(y), length(y)]]

g = [[] for x in range(201)] #note that g[0] is useless

with open('Dijkstra.txt', 'r') as f:
    for line in f.readlines():
        data = line.split()
        node = int(data[0])
        for i in range(1, len(data)):
            n, l = data[i].split(',')
            g[node].append([int(n),int(l)])

#obtain the heap structure
from heapq import heapify, heappush, heappop

s = 1 #the point for which we are calculating the shortest distance for other points
x = [s]
len = [float('inf') for i in range(201)] #used to store shortest path for each vertex - note [0] is useless
path = ['' for i in range(201)] #store the actual path traversed

#initiate dscore for the source point
dscore[s] = 0
#create heap structure
heap = [float('inf') for i in range(201)]
heap[s] = 0

while True:
    for node in x:
        for nei, distance in g[node]:
            if nei in x:
                continue
            heap[nei] = min(heap[nei],distance # update distance 



    


from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print "=== Dijkstra ==="
    print edges
    print "A -> E:"
    print dijkstra(edges, "A", "E")
    print "F -> G:"
    print dijkstra(edges, "F", "G")