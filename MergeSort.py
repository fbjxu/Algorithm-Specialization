def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    while i< len(left):
        result.append(left[i])
        i += 1
    
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result

def Merge_Sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = Merge_Sort(nums[:mid])
    right = Merge_Sort(nums[mid:])
    ans = merge(left, right)

    return ans


test = [3,4,2,1,6]
Merge_Sort(test)