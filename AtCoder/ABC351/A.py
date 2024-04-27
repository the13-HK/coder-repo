A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(0)
else:
    print((sum(A) - sum(B)) + 1)
