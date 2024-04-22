N, Q = map(int, input().split())
n = [list(map(int, input().split())) for _ in range(N)]
q = []
for i in range(Q):
    q.append(int(input()))
max_list = [0, 0, 0, 0]
for i in n:
    x = i[0]
    y = i[1]
    dist = abs(x) + abs(y)
    if x > 0 and y > 0:
        if dist > max_list[0]:
            max_list[0] = dist
    elif x < 0 and y > 0:
        if dist > max_list[1]:
            max_list[1] = dist
    elif x < 0 and y < 0:
        if dist > max_list[2]:
            max_list[2] = dist
    else:
        if dist > max_list[3]:
            max_list[3] = dist

for i in q:
    target = [n[i - 1][0], n[i - 1][1]]
    if target[0] > 0 and target[1] > 0:
        print(max(max_list[0] - abs(target[0]) - abs(target[1]), max_list[1] + abs(target[0]) - abs(target[1]), max_list[2] + abs(target[0]) + abs(target[1]), max_list[3] - abs(target[0]) + abs(target[1])))
    elif target[0] < 0 and target[1] > 0:
        print(max(max_list[0] + abs(target[0]) - abs(target[1]), max_list[1] - abs(target[0]) - abs(target[1]), max_list[2] - abs(target[0]) + abs(target[1]), max_list[3] + abs(target[0]) + abs(target[1])))
    elif target[0] < 0 and target[1] < 0:
        print(max(max_list[0] + abs(target[0]) + abs(target[1]), max_list[1] - abs(target[0]) + abs(target[1]), max_list[2] - abs(target[0]) - abs(target[1]), max_list[3] + abs(target[0]) - abs(target[1])))
    else:
        print(max(max_list[0] - abs(target[0]) + abs(target[1]), max_list[1] + abs(target[0]) + abs(target[1]), max_list[2] + abs(target[0]) - abs(target[1]), max_list[3] - abs(target[0]) - abs(target[1])))