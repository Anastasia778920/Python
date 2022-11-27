# value = None
# print(type(a))
# print(type(b))
# print(type(value))

## Переменные 
a = 123
b = 1.23
value = 12334
s = 'Hello world'
print(s) # вывод строки 
print(a, '-',b, '-', s)
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = True
print(f)

list = ['1', '2', '3', 'hello']
print(list)

## Ввод и вывод данных 
# print() - отвечает за вывыд данных 
# input() - отвечает за ввод данных 

print('Введите a');
a = input()
print('Введите b');
b = input()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')
print(a, ' + ', b, ' = ', a+b) # сложение строк (т.е. 1 + 2 = 12)

print('Введите a');
a = int(input())
print('Введите b');
b = int(input())
print(a, ' + ', b, ' = ', a+b) # сложение чисел (т.е. 1 + 2 = 3)

print('Введите a');
a = float(input())
print('Введите b');
b = float(input())
print(a, ' + ', b, ' = ', a+b) # сложение вещественных значений (т.е 1,5 + 1,5 = 3)

## Арифметические операции 
# +, -, *, /, %, //, **
# занк "**"" - возведение в степень 
a = 123
b = 321
c = a+b
d = a-b
e = a*b
f = a/b
print(c)
print(d)
print(e)
print(f)
# функция round - выведение знаков после запятой, например: 
# a = 1.234543
# b = 3
# c = round(a * b, 5) - цифра 5 это сколько знаков будет после запятой 
# print(c)

# функция присваивания 
a = 3
a += 5 # аналогично это работает и для других арифметических операций (например, *=, /=  и т.д.)
print(a) 

## Логические операции 
# >, >=, <, <=, == (равно), != (не равно)
# not, and, or
# is, is not, in, not in 
# gen
a = 1 > 4 and 5 > 2
print(a)

## Управляющие конструкции: if, if-else

a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a)
else:
    print(b)

username = input('Введите ваше имя: ')
if username == 'Маша':
    print('Блин, это Маша :(')
elif username == 'Марина':
    print('Я так ждала вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)

## Управляющие конструкции: while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)

## Управляющие конструкции: while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)

## Управляющие конструкции: for
for i in 1, -2, 3, 14, 5:
    print(i**2)

r = range(10) #то есть будут выведены числа от 0 до 10 (0, 1 ... 9)
for i in r:
    print(i)



text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text: 
    print(c)



text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

##Списки введение 

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент


## Функции
def f(x):
 return x**2
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType