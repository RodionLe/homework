n = int(input("Введит число n: "))
x = 0
y = 0 
for i in range(n):
    a = int(input("Введите число a: "))
    if i == 0:
        x = a
    if i == 1:
        y = a
sum = x - y
print(sum)