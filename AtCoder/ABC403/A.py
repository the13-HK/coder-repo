N=int(input())
A=list(map(int, input().split()))

sum = 0
for n in range(N):
    if n % 2 == 0:
        sum += A[n]
        
print(sum)