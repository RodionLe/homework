a1 = int(input("Введите число единиц"))
a2 = int(input("Введите число десятков"))
b = int(input("введите простое число "))
x = (a1 + b) % 10
y = a2 + ((a1 + b)//10)
print("TEST 2 Десяток числа -",y,"единица -",x)
