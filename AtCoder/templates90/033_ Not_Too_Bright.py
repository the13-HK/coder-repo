H, W = map(int, input().split())

if H == 1 or W == 1:
    print(H * W)
else:
    h = H // 2
    if H % 2 == 1:
        h += 1
    w = W // 2
    if W % 2 == 1:
        w += 1

    print(h * w)