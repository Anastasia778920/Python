## Реализуйте алгоритм перемешивания списка.
## Из библиотеки random использовать можно только randint

import random 
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Список: ' + str(list))
for i in range (len(list) - 1, 0, -1):
    n = random.randint(0, i + 1)
    list[i], list[n] = list[n], list[i]
print('перемешанный список: ' + str(list))