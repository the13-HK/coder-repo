from bisect import bisect_left

# �������\���l
INF = 2 ** 60

# ����
N = int(input())
A = list(map(int, input().split()))

# �\�[�g���Ă���
A.sort()

# �e�N�G���ɓ�����
Q = int(input())
for _ in range(Q):
    B = int(input())

    # A[j] >= B �ƂȂ�ŏ��� j �����߂�
    j = bisect_left(A, B)

    # A[j] �� A[j-1] ���r����
    res = INF
    if j < N:
        res = min(res, abs(B - A[j]))
    if j > 0:
        res = min(res, abs(B - A[j-1]))

    print(res)