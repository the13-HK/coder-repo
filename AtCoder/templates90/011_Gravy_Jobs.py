N = int(input())
task_list = [list(map(int, input().split())) for _ in range(N)]
task_list.sort()
dp = [[0] * (5001) for _ in range(N+1)]
for i in range(1, N+1):
    task = task_list[i-1]
    for j in range(5001):
        if j < task[1] or j > task[0]:
            dp[i][j] = dp[i - 1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-task[1]] + task[2])

print(max(dp[-1]))