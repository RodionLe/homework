num = int(input("Введите число: "))
new = ""
def F(num):
    global new
    if num > 0:
        x = num % 10   
        x = str(x)
        new = (new + x)
        num = num // 10
        return F(num)
    else:
        return
F(num)
print(new)
