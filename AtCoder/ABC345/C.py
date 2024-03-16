S = input()
N = len(S)
count = 0
for i in range(N):
    tmp = list(S)
    target = set(tmp[i+1:])
    print(target)
    target.discard(tmp[i])
    count += len(target)
print(count)