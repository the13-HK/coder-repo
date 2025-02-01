N, Q = map(int, input().split())
query_list = [input() for _ in range(Q)]
nest = list(range(1, N + 1))
confirm = [1] * N
count = 0

for query in query_list:
    if query == "2":
        print(count)
    else:
        q_list = list(map(int, query.split()))
        p, h = q_list[1], q_list[2]
        before = nest[p - 1]
        nest[p - 1] = h
        confirm[before - 1] -= 1
        confirm[h - 1] += 1
        if confirm[before - 1] == 1:
            count -= 1
        if confirm[h - 1] == 2:
            count += 1
        