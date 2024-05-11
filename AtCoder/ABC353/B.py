N, K = map(int, input().split())
A = list(map(int, input().split()))

empty = K
count = 0
for a in A:
    if empty < a:
        count += 1
        empty = K - a
    else:
        empty -= a
    
    if empty == 0:
        count += 1
        empty = K

if empty < K:
    count += 1
print(count)