N, K = map(int, input().split())

A = list(map(int, input().split()))
start = 0
data = {}
ans = 0
cnt = 0
right = 0
for i in range(N):
    while right < N:
        data.setdefault(A[right], 0)
        if data[A[right]] == 0:
            if cnt == K:
                break
            else:
                cnt += 1
        data[A[right]] += 1
        right += 1
    
    ans = max(ans, right - i)
    if data[A[i]] == 1:
        cnt -= 1
    data[A[i]] -= 1    
print(ans)