# from MergeSort import Merge_Sort

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

def splitClosest(left, right, delta):
    sY = []
    while i < len(left) or j < len(right)


def ClosestPair(Points):
    """
    takes into a collection of points. In other words, an array of points.
    return the pair of points that has the shortest Euclidean Distance

    Assumption: there are no overlapping points
    """
    if len(Points) == 1:
        return Points


    result = []
    for p in Points:
        result.append(p.getX())
    #python uses quick sort for the function sorted: the complexity is O(nlogn)
    sortedPoints = sorted(Points, key = (lambda x: Point.getX(x)))
    midPoint = len(sortedPoints) // 2
    smallerPoints = sortedPoints[:midPoint]
    largerPoints = sortedPoints[midPoint:]

    leftClosest = ClosestPair(smallerPoints)
    leftDist = leftClosest[0].get_dist(leftClosest[1])
    rightClosest = ClosestPair(largerPoints)
    rightDist = rightClosest[0].get_dist(right[1])
    delta = min(leftDist, rightDist)

    xBar = sortedPoints[midPoint].getX()

    #get sY that contains only points whose x-distance from xBar is within delta
    sY = []
    #get points on the left side whose distance to xBar is less than delta
    for p in smallerPoints:
        if abs(p.getX() - xBar) < delta:
            sY.append(p)
    
    for p in largerPoints:
        if abs(p.getX() - xBar) < delta:
            sY.append(p)
    #sort sY

    splitClosest = ClosestSplitPair(smallerPoints, largerPoints, delta)

    if splitClosest == None:
        if leftDist < rightDist:
            return leftClosest
        else:
            return rightClosest

    else:
        return splitClosest


    




    
    return sortedPoints

