N, R, C = map(int, input().split())
S = list(input())
output = []
def move(x, y, s):
    if s == "N":
        return x - 1, y
    elif s == "S":
        return x + 1, y
    elif s == "E":
        return x, y + 1
    elif s == "W":
        return x, y - 1

smoke = [[[0,0]] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    s = S[i-1]
    for j in range(1, i + 1):
        smoke[i][j] = list(move(smoke[i-1][j][0], smoke[i-1][j][1], s))
    if [R,C] in smoke[i]:
        output.append("1")
    else:
        output.append("0")

print("".join(output))
