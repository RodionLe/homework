a = input("Введите число: ")
flag = True

for index, num in enumerate(a):
    if index == 0:
        continue;

    if a[index - 1] > num:
        flag = False
        break;


print(flag)
    #a[index - 1]  сравнение num
    
    