n = int(input("Введите натуральное число n: "))
a = 0
y = -1 
sum = 0 
z = 0
for i in range(1, n + 1):
    z = sum
    y = -y
    a = int(input("Введите натуральное число a "))
    sum = z + (a * y)    
    print(sum)

