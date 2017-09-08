num = int(input("Введите количество человек в группе: "))
weight = None
max = 0
min = 100000000000
tries = 0
x = None
while tries < num:
    x = weight
    weight = int(input("Введите массу человека: "))
    if weight > max:
        max = weight
    elif weight < min:
        min = weight
    tries += 1
if max / min >= 2:
    print("True")
else:
    print(False)