N = int(input())
A = list(map(int, input().split()))
inf = 10 ** 9
# dp[l][r]: l~r�Ԗڂ̐l������������̂ɕK�v�ȃR�X�g
dp = [[inf for i in range(2*N)] for j in range(2*N)]

# ������Ԃ�dp�ɔ��f
for i in range(2*N-1):
    dp[i][i+1] = abs(A[i] - A[i+1])

for kukan in range(2, 2*N):
    for l in range(0, 2*N):
        r = l + kukan
        if r > 2 * N - 1:
            continue
        if (r - l + 1) % 2 == 1:  # ������l������̂Ƃ��̓R�X�ginf
            continue
        dp[l][r] = min(dp[l][r], dp[l+1][r-1] + abs(A[l] - A[r]))
        for k in range(l+1, r):
            dp[l][r] = min(dp[l][r], dp[l][k] + dp[k+1][r])
            # �Ԃ���l�ȏ�̎��͕ʂ̋�ԂƂ��čl�����邽�ߏ��O�ł���

print(dp[0][2*N-1])