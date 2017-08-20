a = int(input("Введите число: "))
c = 3
while a > c:   
    c = c * 3
    if a == c:
        break
if a == c:
    print("Число является степенью числа 3")
else:
    print("Число не является степенью числа 3")
