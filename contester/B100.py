str = input()
mas = str.split(" ")
b = ['+', '-', '*', '//']
a = int(mas[0])
d = mas[1]
c = int(mas[2])
for i in range (len(b)):
    if d == b[i]:
        y = b[i]

if y == '+':
    print(a + c)
if y == '-':
    print(a - c)
if y == '*':
    print(a * c)
if y == '//':
    print(a // c)
    
