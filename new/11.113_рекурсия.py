massif = [1700, 1780, 1990 , 3000, 2139, 2200]
length = len(massif)
Max = massif[0]
n = 0
def find_Max(n, Max):
    if massif[n] > Max:
        Max = massif[n]
           
    if n < length - 1:
        return find_Max(n + 1, Max)
    else:
        return Max
x = find_Max(n, Max)
print(x)
    
massif = [1700, 1780, 1990 , 3000, 2139, 2200]
length = len(massif)
Min = massif[0]
n = 0
def find_Min(n, Min):
    if massif[n] < Min:
        Min = massif[n]
           
    if n < length - 1:
        return find_Min(n + 1, Min)
    else:
        return Min
y = find_Min(n, Min)
print(y)
print(x - y)
    
