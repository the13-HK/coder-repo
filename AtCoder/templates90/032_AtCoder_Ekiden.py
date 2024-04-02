from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
bad = [[] for i in range(N)]
init = 1e10 
ans = init

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    bad[x].append(y)
    bad[y].append(x)

for seq in permutations(range(N)):
    now = seq[0]
    time = A[now][0]
    for i in range(1,N):
        runner = seq[i]
        if runner in bad[now]:
            break
        else:
            now = runner
            time += A[now][i]
    else:
        if time < ans:
            ans = time
            
if ans == init:
    print(-1)
else:
    print(ans)