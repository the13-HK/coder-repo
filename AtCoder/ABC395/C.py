N=int(input())
A= list(map(int, input().split()))
min = N + 1
set_A = set()
target_list= {}
for a in range(N):
    n = A[a]
    if n in set_A:
        hit = target_list[n]
        target = a - hit + 1
        min = target if target < min else min
        target_list[n] = a
    else:
        set_A.add(A[a])
        target_list[n] = a

if min == N + 1:
    print(-1)
else:
    print(min)