N = int(input())

MOD = 10**9+7

f = [0]*(N+1)
f[0] = 1
for n in range(1, N+1):
    f[n] = f[n-1]*n % MOD

finv = [0]*(N+1)
fn = f[N]
fninv = pow(fn, MOD-2, MOD)
finv[N] = fninv
for n in range(N, 0, -1):
    finv[n-1] = finv[n]*n % MOD

def comb(n, k):
    return f[n]*finv[k]*finv[n-k]

for k in range(1, N+1):
    ans = 0
    n = N
    i = 1
    while n >= i:
        ans += comb(n, i)
        i += 1
        n -= k-1
    print(ans % MOD)