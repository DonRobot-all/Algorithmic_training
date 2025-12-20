n = 5  # количество элементов

parent = list(range(n))  # parent[i] = родитель i
rank = [0] * n           # rank[i] = ранг (приближённая высота)

parent = [0, 1, 2, 3, 4]
rank   = [0, 0, 0, 0, 0]


def find(x):
    ...

def union(x, y):
    ...

union(0, 1)
union(1, 2)
union(3, 4)

print(find(0) == find(2))  # True
print(find(0) == find(4))  # False
