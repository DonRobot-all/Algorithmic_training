"""
"""

def correction_permutation(len_array, numbers):
    numbers = list(map(int, numbers.split()))
    all_permutation = set(range(1, len_array + 1))
    s1 = set(numbers)
    all_permutation -= s1
    repeat = set()
    count = 0
    for i in range(len_array):
        if numbers[i] > len_array or numbers[i] in repeat:
            numbers[i] = all_permutation.pop()
            count += 1
        repeat.add(numbers[i])
    return (count, ' '.join(map(str, numbers)))



tasks = {
    (4, '1 100 3 3'): (2, '1 2 3 4'),
    (3, '3 2 1'): (0, '1 2 3')
}
for task in tasks:
    count, permutation = correction_permutation(*task)
    permutation = ' '.join(sorted(permutation.split()))
    print(count, permutation)
    assert (count, permutation) == tasks[task], correction_permutation(*task)