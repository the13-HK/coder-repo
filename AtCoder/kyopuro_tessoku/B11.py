def answer(q:int, A:list):
    left = 0
    right = len(A)
    while left < right:
        mid = ( left + right ) // 2
        if q <= A[mid]:
            right = mid
        else:
            left = mid + 1
    return left

N = int(input())    
A = list(map(int, input().split()))
Q = int(input())
X = []
for _ in range(Q):
    q = int(input())
    X.append(q)

sorted_A = sorted(A)
output_list = []
for x in X:
    ans = answer(x, sorted_A)
    print(ans)