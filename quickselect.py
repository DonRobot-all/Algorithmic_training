def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k > len(left) + len(equal):
        return quickselect(right, k - len(left) - len(equal))
    else:
        return pivot
    

print(quickselect([3,2,3,1,2,4,5,5,6], 4)) # 3 
print(quickselect([3,2,1,5,6,4], 2))
      
# [3,2,3,1,2,4,5,5,6], 6
# [2,1,2][3,3][4,5,5,6], 6
# [4,5,5,6], 6 - 3 - 2 = 1
# [][4][5,5,6]
