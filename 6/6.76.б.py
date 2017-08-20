a = int(input("Введите число: "))
c = 5
while a > c:   
    c = c * 5
    if a == c:
        break
if a == c:
    print("Число является степенью числа 5")
else:
    print("Число не является степенью числа 5")
