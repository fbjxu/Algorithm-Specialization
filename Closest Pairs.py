import math
# from MergeSort import Merge_Sort
#Point Class


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
    
    def getY(self):
        return self.y

    def __str__(self):
        output = '<' + str(self.x) + ',' + str(self.y) + '>'
        return output


def ClosestSplit(sortedPointsX, sortedPointsY, delta):
    #get sY that contains only points whose x-distance from xBar is within delta
    sY = []
    #filtering out points that's far from the midPoint(based on x)
    for p in sortedPointsY:
        if abs(p.getX() - sortedPointsX[len(sortedPointsX)//2].getX()) <= delta:
            sY.append(p)
    shortest = delta
    for i in range(len(sY)-1): #typo in the original lecture
        for j in range(1, min(8,len(sY) - i)): 
            curDis = sY[i].get_dist(sY[i+j])
            if curDis < shortest:
                shortest = curDis
    return shortest

def ClosestPair(Points):
    """
    takes into a collection of points. In other words, an array of points.
    return the pair of points that has the shortest Euclidean Distance

    Assumption: there are no overlapping points
    """

    if len(Points) == 1:
        print('condition points == 1 is hit')
        return math.inf #use math.inf to denote a very large number

    if len(Points) == 2:
        return Points[0].get_dist(Points[1])
    
    # if len(Points) == 3:
    #     return min(Points[0].get_dist(Points[1]), Points[0].get_dist(Points[2]),Points[1].get_dist(Points[2]))

    #divide
    #python uses quick sort for the function sorted: the complexity is O(nlogn)
    sortedPointsX = sorted(Points, key = (lambda x: Point.getX(x))) 
    sortedPointsY = sorted(Points, key = (lambda x: Point.getY(x)))
    midPoint = len(sortedPointsX) // 2
    #split sorted points into two halves: left and right and obtain the shortest distance pair for each half
    leftClosest = ClosestPair(sortedPointsX[:midPoint])
    rightClosest = ClosestPair(sortedPointsX[midPoint:])
    delta = min(leftClosest, rightClosest)
    #conquer
    splitClosest = ClosestSplit(sortedPointsX, sortedPointsY, delta)
    return min(splitClosest, delta)


pointA = Point(2,3)
pointB = Point(12,30)
pointC = Point(40,50)
pointD = Point(5,1)
pointE = Point(12, 10)
pointF = Point(3,4)


array = [pointA, pointB, pointC, pointD, pointE, pointF]

arrayX = sorted(array, key = (lambda x: Point.getX(x)))
arrayY = sorted(array, key = (lambda x: Point.getY(x)))

ClosestPair(array)

arrayTwoData = [(12, 30), (40, 50), (5, 1), (12, 10), (-5, -1)]
arrayTwo = []
for e in arrayTwoData:
    arrayTwo.append(Point(e[0], e[1]))

ClosestPair(arrayTwo)


arrayThreeData = [(0, 0), (-2, 0), (4, 0), (1, 1), (3, 3), (-2,2), (5,2)]
arrayThree = []
for e in arrayThreeData:
    arrayThree.append(Point(e[0], e[1]))

ClosestPair(arrayThree) #1.41421 (0,0) and (1,1)