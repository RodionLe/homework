str = input()
mas = str.split(':')
a = int(mas[0])
b = int(mas[1])
c = int(mas[2])
hours = a * 3600
Min = b * 60
Sum = hours + Min + c
print(Sum)
