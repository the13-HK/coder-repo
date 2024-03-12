A, B, C = map(int, input().split())

def gcd(a,b,c):
    x = a
    y = b
    z = c
    while y > 0:
        x, y = y, x % y
    while z > 0:
        x, z = z, x % z
    return x
g= gcd(A, B, C)
S = A + B + C

print((S//g)-3)