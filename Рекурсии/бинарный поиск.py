number = [5, 12, 24, 34, 46, 70,  90 , 110, 140, 180, 250, 333, 438, 549, 674, 890, 1000]
choice = int(input("Введите число: "))
length = len(number)

def search(choice, left, right):
    x = (right - left) // 2
    p = right - x
    
    if x == 0:
        x = 1
     
    if choice == number[p]:
        return p
    
    if right == left:        
        return -1       
    
    if choice > number[p]:        
        return search(choice, left + x, right)
    else: 
        return search(choice, left, right - x)
        
result = search(choice, 0, length - 1)

print(result)
