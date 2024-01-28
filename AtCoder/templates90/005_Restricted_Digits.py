# MOD
MOD = 1000000007

# N �̑ΐ�
LOG = 62

# ����
N, B, K = map(int, input().split())
C = list(map(int, input().split()))

# dp[i] �� dp[j] ���|�����킹�� dp[i+j] �𓾂�֐�
# tj: 10^j �� B �Ŋ��������܂�
def mul(dpi, dpj, tj):
    res = [0] * B
    for p in range(B):
        for q in range(B):
            res[(p * tj + q) % B] += dpi[p] * dpj[q]
            res[(p * tj + q) % B] %= MOD
    return res

# ten[i]: 10^(2^i) �� B �Ŋ��������܂�
ten = [10] * LOG
for i in range(1, LOG):
    ten[i] = (ten[i - 1] * ten[i - 1]) % B

# dp[2^i][r] �� doubling[i][r] �Ə������Ƃɂ���
doubling = [[0] * B for _ in range(LOG)]

# ������ (doubling[0] = dp[1])
for k in range(K):
    doubling[0][C[k] % B] += 1

# �_�u�����O
for i in range(1, LOG):
    doubling[i] = mul(doubling[i - 1], doubling[i - 1], ten[i - 1])

# �_�u�����O�������ʂ����Ƃɓ��������߂�
res = [0] * B
res[0] = 1
for i in range(LOG):
    if N & (1 << i):
        res = mul(res, doubling[i], ten[i])
print(res[0])