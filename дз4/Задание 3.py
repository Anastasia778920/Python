## Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
## Пример
## - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

n = list('1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9')

list = n
print(list)

list_count = []
for i in list:
    count = 0 
    for a in list:
        if a == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []

for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print(result)