N = int(input())
a1 = int(input())
Sum = a1
M_sum = a1
for i in range(N - 1):
    a = int(input())
    if a < Sum + a:
        Sum += a
    else:
        Sum = a
    if Sum > M_sum:
        M_sum = Sum
print(M_sum)
         
    
