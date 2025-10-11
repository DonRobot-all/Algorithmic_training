from math import sqrt
from collections import Counter


data = [
    [170, 65, 'М'],
    [180, 80, 'М'],
    [160, 50, 'Ж'],
    [155, 45, 'Ж']
]

new_point = [167, 55]
k = 3  # количество соседей


def pythagoras_distance(p1, p2):
    a = p1[0] - p2[0]
    b = p1[1] - p2[1]
    c = sqrt(a**2 + b**2)
    return c


def knn_classify(data, new_point, k):
    distances = []
    for item in data:
        features = item[:-1]
        label = item[-1]
        dist = pythagoras_distance(features, new_point)
        distances.append((dist, label))
    
    distances.sort(key=lambda x: x[0])
    k_nearest = distances[:k]
    
    labels = [label for _, label in k_nearest]
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common

result = knn_classify(data, new_point, k)
print(f"Новый объект с параметрами {new_point} классифицирован как: {result}")
# Новый объект с параметрами [167, 55] классифицирован как: Ж
