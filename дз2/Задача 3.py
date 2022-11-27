## Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
## Пример:
## - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52] -> 14.072  (Округлять не обязательно)

n = int(input('введите число N: '))
def in_list(n):
    list = []
    for i in range (1, n + 1):
        list.append((1 + 1 / i) ** i)
    return list
def sum(list):
    sum = 0 
    for i in range (len(list)):
        sum = sum + list [i]
    return sum 
list = in_list(n)
print(list)
result = sum(list)
print(result)