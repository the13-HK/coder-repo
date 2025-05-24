N, K = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = N

if A[-1] < K:
    print(-1)
else:
    while start < end:
        mid = (start + end) // 2
        target = A[mid]
        if K > target:
            start = mid + 1
        elif K < target:
            end = mid
        else:
            start = end = mid
    print(start)