## предложить улучшения кода для четырёх уже решённых задач:
## С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
## Начиная с 3 семинара.

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print(sum)
