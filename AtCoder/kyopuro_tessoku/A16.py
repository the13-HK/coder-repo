N=int(input())
A=list(map(int, input().split()))
B=list(map(int,input().split()))

ans=[0] * N
ans[0] = 0
ans[1] = A[0]

for i in range(2, N):
    ans[i] = min(ans[i - 2] + B[i - 2] , ans[i - 1] + A[i - 1])

print(ans[-1])