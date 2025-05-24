A, B = map(int, input().split())

q = A // B
r = A % B
if r < (B // 2 + 1):
    print(q)
else:
    print(q + 1)