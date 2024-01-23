n, l = map(int, input().split())
k = int(input())
an = list(map(int, input().split()))

def check(x):
    cnt = 0
    pre = 0
    for i in range(n):
        if an[i] - pre >= x:
            cnt += 1
            pre = an[i]
            
    if l - pre >= x:
        cnt += 1
    
    return (cnt >= k + 1)

left, right = -1, l + 1
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)