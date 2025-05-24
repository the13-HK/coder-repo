N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(S + 1):
        a = A[i - 1]
        if j < a:
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
        else:
            if dp[i - 1][j] == 1 or dp[i - 1][j - a] == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

if dp[N][S] == 1:
    print("Yes")
else:
    print("No")