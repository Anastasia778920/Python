## Напишите программу, удаляющую из файла все слова, содержащие "абв".

path = ''
with open(path, 'r', encoding='utf8')as file:
    text = file.readline().split()

print(text)
find = 'абв'

for word in text:
    if find in word:
        text.remove((word))
    
print(text)