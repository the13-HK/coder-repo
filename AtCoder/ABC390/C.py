H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

#初期設定
r, l = -1, -1
u, d = -1, -1

#網羅的に範囲を探索する。今回は1000×1000なので、全探索でも間に合う。
for i in range(H):
    inv = H - i - 1
    for j in range(W):
        if S[i][j] == "#" and u < 0:
            u = i
        if S[inv][j] == "#" and d < 0:
            d = inv

for i in range(W):
    inv = W - i - 1
    for j in range(H):
        if S[j][i] == "#" and l < 0:
            l = i
        if S[j][inv] == "#" and r < 0:
            r = inv

if r < 0:
    flag = 0
    for i in S:
        for j in i:
            if j == "#" or j == "?":
                flag = 1
    print("Yes" if flag == 1 else "No")

else:
    flag = 0
    for i in range(u, d + 1):
        for j in range(l, r + 1):
            if S[i][j] == ".":
                flag = 1
    print("Yes" if flag == 0 else "No")