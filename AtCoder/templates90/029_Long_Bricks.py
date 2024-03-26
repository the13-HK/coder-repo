W, N = map(int, input().split())
list = [0] * (W + 2)

for i in range(N):
    l, r = map(int, input().split())
    h = max(list[l:r + 1]) + 1
    list[l:r + 1] = [h] * (r - l + 1)
    print(h)
