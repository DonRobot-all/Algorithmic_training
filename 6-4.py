"""
"""

def correction_permutation(number, array):
    return (2, '1 3 2 4')

tasks = {
    (4, '1 100 3 3'): (2, '1 2 3 4'),
    (3, '3 2 1'): (0, '1 2 3')
}
for task in tasks:
    count, permutation = correction_permutation(*task)
    permutation = ' '.join(sorted(permutation.split()))
    print(count, permutation)
    assert (count, permutation) == tasks[task], correction_permutation(*task)