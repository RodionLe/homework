num = input("Введите натуральное число: ")

x = False
y = False

for n in num:
   if n == '2':
        x = True
        break

   if n == '5':
        y = True
        break
if y:
    print("5")
elif x:
    print("2")
else:
    print("(")