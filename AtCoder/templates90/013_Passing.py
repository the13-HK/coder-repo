N, M = map(int, input().split())

select = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, input().split())
    select[a - 1].append((b - 1, c))
    select[b - 1].append((a - 1, c))

ans = [0]*N
import heapq
inf = 10**9
tfrom1 = [inf]*N
checkfrom1 = [False]*N
q = [(0, 0)]

while q:
    cost, v = heapq.heappop(q)
    if checkfrom1[v]:
        continue
    checkfrom1[v] = True
    tfrom1[v] = cost
    for to, c in select[v]:
        if checkfrom1[to]:
            continue
        heapq.heappush(q, (cost + c, to))
        
tfromN = [inf]*N
checkfromN = [False]*N
q = [(0, N-1)]
while q:
    cost, v = heapq.heappop(q)
    if checkfromN[v]:
        continue
    checkfromN[v] = True
    tfromN[v] = cost
    for to, c in select[v]:
        if checkfromN[to]:
            continue
        heapq.heappush(q, (cost + c, to))
        
for i in range(N):
    print(tfrom1[i] + tfromN[i])