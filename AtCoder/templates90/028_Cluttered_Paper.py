N = int(input())
duplicate = [[0] * 1002 for _ in range(1002)]
value_count = [0] * (N+1)

for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    duplicate[lx][ly] += 1
    duplicate[rx][ry] += 1
    duplicate[lx][ry] -= 1
    duplicate[rx][ly] -= 1
for i in range(1001):
    for j in range(1001):
        duplicate[i][j] += duplicate[i][j-1]
        
for i in range(1001):
    for j in range(1001):
        duplicate[j][i] += duplicate[j-1][i]
        value_count[duplicate[j][i]] += 1

for i in range(1, N+1):
    print(value_count[i])