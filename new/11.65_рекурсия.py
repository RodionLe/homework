February = [1, 0, 3, 4, 3, 5,0, 0]
length = len(February)
count = 0
def F(n):
    count = 0
    if February[n] == 0:
        count = 1
        
    if n > 0:        
        return count + F(n - 1)
    else:
        return count
        
count = F(length - 1)
print(count)
