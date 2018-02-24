#пункт А

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(numbers)

for i in range (length):
    numbers[i] *= 2

print("Пункт А", numbers)

#пункт Б

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = int(input("Введите число А: "))

for i in range (length):
    numbers[i] -= A

print("Пункт Б", numbers)

#Пункт В

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = numbers[0]

for i in range (length):
    numbers[i] = numbers[i] // x

print("Пункт В", numbers)
