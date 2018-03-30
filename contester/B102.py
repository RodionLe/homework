str = input()
mas = str.split(' ')
a = int(mas[0])
b = int(mas[1])
c = int(mas[2])
x = None
lenght = len(mas)
if a > b:
    x = a
    a = b
    b = x
if b > c:
    x = b
    b = c
    c = x
if a > b:
    x = a
    a = b
    b = x
print(a,b,c)
