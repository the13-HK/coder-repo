N, M = map(int, input().split())
graph = []

node_collection = [0] * N

for _ in range(M):
    graph.append(list(map(int, input().split())))

for g in graph:
    from_node = g[0] - 1
    to_node = g[1] - 1
    if node_collection[from_node] == 0 or node_collection[from_node] == 1:
        node_collection[from_node] += 1
        if node_collection[to_node] == 0 or node_collection[to_node] == 1:
            node_collection[to_node] += 1
        else:
            break
    else:
        break

if node_collection.count(2) == N:
    print("Yes")
else:
    print("No")
