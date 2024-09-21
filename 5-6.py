"""
Никакие два цикла не пересекаются друг с другом, т. е.
любая перестановка распадается на набор отдельных циклов. В самом деле, если бы
два цикла пересекались, то существовал бы общий элемент х, в который переходят
два различных элемента. Однако тогда в двух позициях перестановки должно было
быть записано одно и то же число х, что невозможно по определению перестановки.
"""

numbers = list(map(int, input().split()))
answer = 0
for idx in range(0, len(numbers)):
    current_number = idx
    while numbers[current_number] != -1:
        numbers[current_number], current_number = -1, numbers[current_number] - 1
        if numbers[current_number] == -1:
            answer += 1

print(answer)