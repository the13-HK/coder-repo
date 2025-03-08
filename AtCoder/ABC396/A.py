N=int(input())
A= list(map(int, input().split()))

count = 0
prev = 0
for i in range(N):
    if A[i] == prev:
        count += 1
    else:
        count = 0
    prev = A[i]
    if count == 2:
        print("Yes")
        exit()
print("No")