# res[i][c] := i �����ڈȍ~�ōŏ��ɕ��� c ���o�ꂷ�� index
# ���݂��Ȃ��Ƃ��� N
def calc_next(S):
    # ������ S �̒���
    N = len(S)

    # ����
    res = [[N] * 26 for _ in range(N + 1)]

    # ��납�猩��
    for i in range(N - 1, -1, -1):
        # i + 1 �����ڈȍ~�̌��ʂ���U i �����ɃR�s�[
        for j in range(26):
            res[i][j] = res[i + 1][j]

        # i �����ڂ̏��𔽉f������
        res[i][ord(S[i]) - ord('a')] = i

    # ������Ԃ�
    return res

# ����
N, K = map(int, input().split())
S = input()

# �O����
res = ''
nex = calc_next(S)

# �×~�@
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]

        # ������ K ����������� OK
        if N - k >= K - i:
            res += chr(ord('a') + ordc)
            j = k
            break
print(res)