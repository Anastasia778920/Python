## Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('Введите номер четверти, в которой будут показаны диапазон возможных координат точек в указанной четверти: '))

if a == 1:
    print('В 1-ой четверти: х > 0 и y > 0')
elif a == 2:
    print('Во 2-ой четверти: х < 0 и y > 0')
elif a == 3:
    print('В 3-й четверти: х < 0 и y < 0')
elif a == 4:
    print('В 4-ой четверти: х > 0 и y < 0')
else:
    print('Такой четверти не существует')

