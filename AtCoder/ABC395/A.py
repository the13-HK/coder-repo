N=int(input())
A= list(map(int, input().split()))

prev = 0
for i in range(N):
    if A[i] > prev:
        prev = A[i]
    else:
        print("No")
        exit()
print("Yes")