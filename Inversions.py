def countSplitInv(left, right):
    """
    input takes a list of length n 
    output the number of split inversions
    """

    i = 0 
    j = 0 

    invCount = 0
    sortedArray = []

    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            sortedArray.append(left[i])
            i += 1
        
        else:
            sortedArray.append(right[j])
            j += 1
            leftRes = len(left) - i
            invCount += leftRes
            
            
    while i < len(left):
        sortedArray.append(left[i])
        i += 1
    
    while j < len(right):
        sortedArray.append(right[j])
        j += 1

    return (sortedArray, invCount)

# #test
# left = [1,5,9]
# right = [2,4,6]
# print(countSplitInv(left, right))


def Inversions(l):
    """
    input is a list of numbers
    output returns the number of inversions within the provided list
    """

    #base cases
    if len(l) < 2:
        return (l, 0)

    else:
        mid = len(l) // 2
        leftL, leftInv = Inversions(l[:mid])
        rightL, rightInv = Inversions(l[mid:])
        sortedL, splitInv = countSplitInv(leftL, rightL)

        invCount = leftInv + rightInv + splitInv
        return (sortedL, invCount)

with open("homework.txt", "r") as fd:
    lines = fd.read().splitlines()

num = []
for l in lines:
    num.append(int(l))

print(Inversions(num))
    
