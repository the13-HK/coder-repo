N = int(input())
S = input()

search = "atcoder"
mod = 10 ** 9 + 7

dp = [[0]*(len(search)+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(len(search)+1):
        dp[i+1][j] = (dp[i][j] + dp[i+1][j]) % mod   
        if j < len(search) and S[i] == search[j]:
            dp[i+1][j+1] = (dp[i][j] + dp[i+1][j+1]) % mod    

print(dp[N][len(search)])