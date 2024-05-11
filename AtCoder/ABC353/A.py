N = int(input())
H = list(map(int, input().split()))

target = H[0]
count = 0
for h in range(N):
    if H[h] > target:
        count = h + 1
        break
    else:
        continue
if count == 0:
    print(-1)
else:
    print(count)