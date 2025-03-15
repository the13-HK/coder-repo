N = int(input())
A = list(map(int, input().split()))

left_A = {}
for i in range(N):
    left_A[A[i]] = left_A.get(A[i], 0) + 1

right_A = {}
max_A = len(left_A)

if len(left_A) == N:
    print(N)
else:
    for i in A:
        left_A[i] -= 1
        if left_A[i] == 0:
            left_A.pop(i)
        right_A[i] = right_A.get(i, 0) + 1
        
        if len(right_A) + len(left_A) > max_A:
            max_A = len(right_A) + len(left_A)
    print(max_A)
        