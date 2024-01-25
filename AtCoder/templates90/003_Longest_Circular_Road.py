n = int(input())
list = [[] for _ in range(n)]
for i in range(1,n):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    list[a].append(b)
    list[b].append(a)
    
def dfs (s):
    dist = [-1] * n
    dist[s] = 0
    
    stack = [s]
    while stack:
        v = stack.pop()
        for i in list[v]:
            if dist[i] == -1:
                stack.append(i)
                dist[i] = dist[v] + 1
    return dist
                
dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)