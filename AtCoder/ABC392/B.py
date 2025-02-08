N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
list = range(1,N + 1)
output = []

for i in range(1,N + 1):
    if  A.count(i) ==0:
        output.append(i)
    else:
        continue
print(len(output))
if len(output) != 0:
    print(*output)