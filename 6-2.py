"""
Заметим, что подсаживать имеет смысл только деревья с пороговым числом
а = 0, потому что использование деревьев с большими числами позволит достичь
либо такого же, либо худшего результата.
Для решения задачи будем рассматривать деревья в порядке увеличения (или, если
быть точным, неубывания) их пороговых величин — попросту говоря, отсортируем
массив а; обозначим отсортированный массив через Ь. Чтобы зацвело первое дере
во в этом порядке, очевидно, недостает Ь дополнительных деревьев. Чтобы зацвело 
второе дерево, недостает b2 - 1 дополнительных деревьев (считая, что цветение
первого дерева мы обеспечили). Продолжая эту логику, получаем, что для цветения
i-ro дерева требуется подсадит b - i - 1 дополнительных деревьев. Таким образом,
ответом ко всей задаче является следующая величина:
max {bi - i - 1}.
"""

n = int(input())
nums = list(map(int, input().split()))
b = sorted(nums)
ans = max(number - idx for idx, number in enumerate(b))
print(ans)