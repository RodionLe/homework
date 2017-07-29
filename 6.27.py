x = int(input("Введите натуральное число: "))
tries = 0
a = x // 10
while x != 0:
    b = x % 10
    if a > 10:
        tries += 1
        a = a // 10
  
