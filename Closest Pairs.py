from MergeSort import Merge_Sort

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_dist(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        dist = (delta_x**2 + delta_y**2)**0.5
        return dist

    def getX(self):
        return self.x

    def __str__(self):
        output = '<' + str(self.x) + ',' + str(self.y) + '>'
        return output


def ClosestPair(Points):
    """
    takes into a collection of points. In other words, an array of points.
    return the pair of points that has the shortest Euclidean Distance
    """
    # step one, find x-bar (the mid point, in terms of x, of all the points passed in)
    result = []
    for p in Points:
        result.append(p.getX())
    
    sortedX = Merge_Sort(result)
    
    return sortedX




pointA = Point(1,2)
pointB = Point(0,0)
Points = [pointA, pointB]
test = ClosestPair(Points)
print(test)

