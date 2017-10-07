x = None
y = None
def happy_numbers():
    number = input("Введите число: ")
    length = len(number)
    x = int(number[0]) + int(number[1]) + int(number[2])    
    y = int(number[length - 1]) + int(number[length - 2]) + int(number[length - 3])
    if x == y:
        return print("Это счастливое число")
    else:
        return print("Это не счастливое число")
happy_numbers()


