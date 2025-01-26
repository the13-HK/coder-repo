X=int(input())

N=1
while X > 1:
    N += 1
    X = X // N
print(N)