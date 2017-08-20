a = input("Введите  число: ")
length = len(a)
x =""
for i in range(length):
    y = a[length -1 - i]
    x = x + y 
print(int(x))