N, W = map(int, input().split())
mass = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
check = [list(map(int, input().split())) for _ in range(Q)]
max_check = max(check, key=lambda x: x[0])
print(max_check)

line = [[0] * W ] * 10 ** 9
for i, m in enumerate(mass):
    line[m[0]][m[1]] = i

t = 0
