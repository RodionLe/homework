a = input("Введите число: ")
x = len(a)
n = 2
y = a[x + 1 - n] # последняя цифра
z = a[x - n] #Пред
tries = 1
while x + 1 != n or tries == x + 1:
    y = a[x + 1 - n]
    z = a[x - n]
    tries += 1
    if y < z:
        n += 1
    else:
        break
if n > x:
    print("True")
else:
    print("False")
    
