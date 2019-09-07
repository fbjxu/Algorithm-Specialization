import random
def choosePivot(array,l, r):
    return random.randint(l,r)

def partition(array, l, r, count):
    """
    takes in a pivot and an arrya
    returns two sub-arrays 
    """
    # pivot = choosePivot(array, l, r)
    # print(array)
    pivot = choosePivot(array,l,r)
    # print('selected pivot', pivot, 'with value: ', array[pivot])
    array[pivot], array[l] = array[l], array[pivot]
    count[0] += (r-l)
    i = l+1 

    for j in range(l+1, r+1):   
        if array[j]<array[l]:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i-1], array[l] = array[l], array[i-1]
    return (i-1)

def quisckSortinside(array, l, r,count):
    if l < r:
        j = partition(array, l, r, count)
        quisckSortinside(array, l, j-1, count)
        quisckSortinside(array, j+1, r, count)
    return array, count[0]
        
def quickSort(array):
    l = 0
    r = len(array) - 1
    count = [0]
    res = quisckSortinside(array, l, r, count)
    return res


# array = [3,1,2,5,69,6, 23,4]
# quickSort(array)

data = []

with open ('quicksortdata.txt') as file:
    for line in file.readlines():
        data.append(int(line))

qsdata, qscount = quickSort(data)

sorteddata = sorted(data)

check = sorteddata == qsdata
if check == True:
    print("count:", qscount)




