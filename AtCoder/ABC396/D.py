N, Q = map(int, input().split())
op = [ list(map(int, input().split())) for _ in range(Q) ]
nest = [[]] 
current = {0:-1}
for i in range(1, N + 1):
    nest.append([i])
    current[i] = i

for action_unit in op:
    action = action_unit[0]
    if action == 1:
        x, y = action_unit[1], action_unit[2]
        pre = current[x]
        nest[pre].remove(x)
        nest[y].append(x)
        current[x] = y
    elif action == 2:
        x, y = action_unit[1], action_unit[2]
        x_nest = nest[x]
        y_nest = nest[y]
        nest[x] = y_nest
        nest[y] = x_nest
        for j in x_nest:
            current[j] = y
        for j in y_nest:
            current[j] = x
    elif action == 3:
        x = action_unit[1]
        print(current[x])
    