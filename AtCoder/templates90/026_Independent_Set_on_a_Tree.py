#026 - Independent Set on a Tree（★4）
N = int(input())
G = [[] for i in range(N)]

for i in range(N-1):
    A,B = map(int,input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

#探索用のスタック
st = [0]
dist = [-1] * N
dist[0] = 0
even = [1]
odd = []

while st:
    v = st.pop()

    for v2 in G[v]:
        if dist[v2] == -1:
            st.append(v2)
            dist[v2] = dist[v] + 1
            if dist[v2] % 2 == 0:
                even.append(v2+1)
            else:
                odd.append(v2+1)

if len(even) >= len(odd):
    print(*even[:N//2])
else:
    print(*odd[:N//2])



