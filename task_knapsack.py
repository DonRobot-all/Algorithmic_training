# (название, вес, ценность)
items = [
    ("Магнитофон", 4, 3000),
    ("Ноутбук", 3, 2000),
    ("Гитара", 1, 1500),
    ("iphone", 1, 2000)
]

capacity = 4  # вместимость рюкзака (в кг)

# --- Жадный алгоритм ---
def greedy_knapsack(items, capacity):
    # сортируем предметы по "ценность / вес" (от большего к меньшему)
    items_sorted = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total_value = 0   # общая ценность предметов в рюкзаке
    total_weight = 0  # текущий вес рюкзака
    chosen = []       # список выбранных предметов

    for name, weight, value in items_sorted:
        # если вещь помещается в рюкзак, берём её
        if total_weight + weight <= capacity:
            chosen.append(name)
            total_weight += weight
            total_value += value

    return total_value, chosen


# --- Динамическое программирование ---
def dp_knapsack(items, capacity):
    n = len(items)

    # dp[i][w] = максимальная ценность, которую можно набрать,
    # используя первые i предметов и рюкзак вместимостью w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Заполняем таблицу построчно
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]  # текущий предмет
        for w in range(1, capacity + 1):
            if weight <= w:
                # либо не берём предмет (dp[i-1][w]),
                # либо берём его и добавляем его ценность (dp[i-1][w-weight] + value)
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # если предмет не помещается, просто копируем предыдущее значение
                dp[i][w] = dp[i - 1][w]

    # Восстанавливаем список выбранных предметов (обратный ход)
    chosen = []
    w = capacity
    for i in range(n, 0, -1):
        print(dp[i][w], dp[i - 1][w])
        # если значение изменилось, значит, предмет был взят
        if dp[i][w] != dp[i - 1][w]:
            name, weight, value = items[i - 1]
            chosen.append(name)
            w -= weight  # уменьшаем доступный вес

    return dp[n][capacity], list(reversed(chosen))

greedy_result = greedy_knapsack(items, capacity)
dp_result = dp_knapsack(items, capacity)

print("Жадный алгоритм:", greedy_result)
print("Динамическое программирование:", dp_result)


# def knapsack(weights, values, W):
#     n = len(weights)
#     # dp[i][w] = макс. ценность при использовании первых i предметов и вместимости w
#     dp = [[0] * (W + 1) for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         for w in range(W + 1):
#             if weights[i-1] <= w:
#                 # либо берем предмет i-1, либо нет
#                 dp[i][w] = max(dp[i-1][w],
#                                dp[i-1][w - weights[i-1]] + values[i-1])
#             else:
#                 # не можем взять предмет i-1
#                 dp[i][w] = dp[i-1][w]
#             print(dp[i])

#     return dp[n][W]  # максимальная ценность

# weights = [2, 3, 4, 5]   # веса предметов
# values = [3, 4, 5, 6]    # ценности предметов
# W = 5                    # вместимость рюкзака

# print(knapsack(weights, values, W))  # вывод: 7

items = [
    ("Золото", 10, 600),
    ("Серебро", 20, 1000),
    ("Бронза", 30, 900),
]
W = 25

max_value, chosen_items = fractional_knapsack(items, W)

print("Максимальная ценность:", max_value)
print("Выбранные предметы:")
for name, weight, value in chosen_items:
    print(f"{name}: взято {weight} единиц, ценность {value}")
