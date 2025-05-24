N, K = map(int, input().split())
num_seq = [1] * (N + 1)
n = 1 * K

for i in range (K, N + 1):
    num_seq[i] = n
    n -= num_seq[i - K]
    n += num_seq[i]
    n %= 10 ** 9

print(num_seq[N])