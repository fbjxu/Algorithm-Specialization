"""
features needed for the class
verticies
edges
ordering/finishing time
explored or not

"""
class Node(object):
    def __init__(self, vertex, edges):
        self.vertex = vertex #name of vertex
        self.edges = edges #list of edges the node points to
        self.explored = False #inidcate if the node has been explored or not
        self.fTime = None #int that indicate the finishing time
    def getVertex(self):
        return self.vertex
    
    def getExplored(self):
        return self.explored

    def __str__(self):
        s = '' #store edge info
        for i in self.edges:
            s += str(i)
            s += ' '
        output = 'name: '+ str(self.vertex) + ' edges: [' + s+']' + ' FTime: ' + str(self.fTime) +' Explored: ' + str(self.explored)
        return output
    def setFTime(self, time):
        self.fTime = time
    
    def getFTime(self):
        return self.fTime
    
    def setExplored(self, status):
        self.explored = status

class Graph(object):
    def __init__(self):
        self.nodes = [] #store a list of nodes
    
    def getNode(self, name):
        for node in self.nodes:
            if node.getVertex() == name:
                return node
    
    def addNode(self, node):
        self.nodes.append(node)

    def __str__(self):
        result = ''
        for node in self.nodes:
            result+= 'Node '
            result += Node.__str__(node)
            result += '\n'
        return result


def readgraph(filename):
    """
    input: filename in txt format
    output: dictionary of the format {a:b} where a shows the vertex name and b is the list of 
    the verticies the vertex points to
    """
    res = {}
    with open(filename, 'r') as data:
        for line in data.readlines():
            edge = line.split()
            if edge[0] in res.keys():
                res[edge[0]].append(edge[1])
            else:
                res[edge[0]] = [edge[1],]
    return res

def readgraphRev(filename):
    """
    input: filename in txt format
    output: dictionary of the format {a:b} where a shows the vertex name and b is the list of 
    the verticies the vertex points to
    """
    res = {}
    with open(filename, 'r') as data:
        for line in data.readlines():
            edge = line.split()
            if edge[1] in res.keys():
                res[edge[1]].append(edge[0])
            else:
                res[edge[1]] = [edge[0],]
    return res

def createGraph(data):
    graph = Graph()
    for e in data.keys():
        node = Node(e, data[e])
        graph.addNode(node)
    return graph
# def DFSLoop(graph, ordering = garph.keys()):

def DFS(Graph, s):
    """
    input: a graph and a vertex s
    output: a map that maps vertex -> finishing time
    """
    if s != None:
        if s.getExplored() == False:
            s.setExplored(True)
            for edge in s.edges: #edge is a string
                v = Graph.getNode(edge)
                DFS(Graph, v) #recursive call
            s.setFTime(t[0])
            t[0] += 1
    return 

def DFSLoop(Graph):
    if Graph.nodes[0].getFTime() != None:
        orderedNodes = sorted(Graph.nodes, key= Node.getFTime, reverse = True)
    else:
        orderedNodes = Graph.nodes   
    for node in orderedNodes:
        DFS(Graph, node)

            
        

# G = Graph()
# a = Node('1', ['2'])
# b = Node('2', ['3'])
# c = Node('3', ['4'])
# d = Node('4', ['5'])

# G.addNode(a)
# G.addNode(b)
# G.addNode(c)
# G.addNode(d)

# t = [1]
# DFSLoop(G)
# print(G)



if __name__ == '__main__':
    data_dict = readgraph("SCC.txt")
    data_dict_rev = readgraphRev("SCC.txt")
    g = createGraph(data_dict)
    gRev = createGraph(data_dict_rev)
    DFSLoop(gRev)

    


elements = [0]
def DFS(Graph, s):
    """
    input: a graph and a vertex s
    output: a map that maps vertex -> finishing time
    """
    if s != None:
        if s.getExplored() == False:
            s.setExplored(True)
            elements[0] += 1
            for edge in s.edges: #edge is a string
                v = Graph.getNode(edge)
                DFS(Graph, v) #recursive call
            s.setFTime(t[0])
            t[0] += 1
    return 