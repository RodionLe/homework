a = int(input("Введите натуральное число "))
tries = 1
while tries != 20 or a % 10 == 7:
    tries +=1
    print(tries)
    a = int(input("введите натуральное число"))
    x = a % 10
    
    if x == 7:
        print(tries)
        break
