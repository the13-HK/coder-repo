W, N = map(int, input().split())
recipes = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N + 1) for _ in range(N + 1)]
list = []
max = -1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + recipes[j - 1], dp[i][j - 1], dp[i - 1][j - 1] + recipes[i - 1][1] if recipes[i - 1][0] <= W else 0)
        list.append(dp[i][j])