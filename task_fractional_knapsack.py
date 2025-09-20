def fractional_knapsack(items, W):
    # сортировка по value/weight
    items_sorted = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
    total_value = 0
    chosen = []

    for name, weight, value in items_sorted:
        if W == 0:
            break
        if weight <= W:
            # берём весь предмет
            chosen.append((name, weight, value))
            W -= weight
            total_value += value
        else:
            # берём часть предмета
            fraction = W / weight
            chosen.append((name, W, value * fraction))
            total_value += value * fraction
            W = 0

    return total_value, chosen
