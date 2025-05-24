N, M, Q = map(int, input().split())

can_view = [set() for _ in range(N)]
can_view_all = [False] * N
for _ in range(Q):
    t, *q = map(int, input().split())
    x = q[0] - 1
    if t == 1:
        y = q[1] - 1
        can_view[x].add(y)
    elif t == 2:
        can_view_all[x] = True
    else:
        y = q[1] - 1
        print("Yes" if can_view_all[x] or y in can_view[x] else "No")

    