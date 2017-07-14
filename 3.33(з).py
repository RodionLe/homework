x = int(input("Введите x "))
y = int(input("Введите y "))
if x <= 1 and y >= 1.5:
    print("Истина")
elif x >= 1 and x <= 2.5 and y >= -2:
    print("Истина")
elif x >= 2.5 and y >= 1.5:
    print("Истина")
else:
    print("Лож")
