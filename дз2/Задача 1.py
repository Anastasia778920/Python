## Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
## Пример:
## - 6782 -> 23
## - 0.56 -> 11

number = input('Введите вещественое число: ')
def sum (number):
    sum = 0 
    for i in number:
        if i != '.':
            sum = sum + int(i)
    return sum 
print(sum(number))