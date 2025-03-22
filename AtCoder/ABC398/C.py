N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)
pre_v = -1
pre_max = -1
max_v = -1

for v in sorted_A:
    if v == pre_v:
        max_v = -1
        continue
    else:
        pre_max = max_v
        pre_v = v
        if pre_max != -1:
            break
        else:
            max_v = v
        
if max_v == -1:
    print(-1)
else:
    print(A.index(max_v) + 1)