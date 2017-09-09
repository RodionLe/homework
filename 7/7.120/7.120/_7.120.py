num = int(input("Введите количество человек в группе: "))
weight = int(input("Введите массу человека: "))

max = min = weight
tries = 1
while tries < num:
    
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