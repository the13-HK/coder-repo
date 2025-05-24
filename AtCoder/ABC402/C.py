N, M = map(int, input().split())

recipe_list = []
day = [0] * N
for m in range(M):
    recipe = set(list(map(int, input().split()))[1:])
    recipe_list.append(recipe)
B = list(map(int, input().split()))

B.reverse();
for r in recipe_list:
    for v, i in enumerate(B):
        if i in r:
            day[v] += 1
            break

count = 0
for i in reversed(day):
    count += i
    print(count)