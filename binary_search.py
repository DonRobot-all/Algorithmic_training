def binary_search(list, target):
    low = 0
    right = len(list) - 1
    while low <= right: 
        mid = (low + right) // 2 
        number = list[mid]
        if number == target: 
            return mid
        elif number > target:
            right = mid - 1
        else: 
            low = mid + 1
    return None 
my_list = [1, 3, 5, 7, 9] 
print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None
