x = None
y = None
number = 100000
def happy_numbers(number):
    number = str(number)
    length = len(number)
    x = int(number[0]) + int(number[1]) + int(number[2])    
    y = int(number[length - 1]) + int(number[length - 2]) + int(number[length - 3])
    if x == y:
        return print("Это число", number, "счастливое")
    else:
        return print("Это число", number, "не счастливое")
while number < 10000000:
    happy_numbers(number)
    number += 1
