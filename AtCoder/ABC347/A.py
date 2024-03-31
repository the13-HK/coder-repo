N, K = map(int, input().split())
A = list(map(int, input().split()))
devide_list = []

for i in A:
    if i % K == 0:
        devide_list.append(i // K)
    else:
        continue
        
print(" ".join([str(_) for _ in sorted(devide_list)]))