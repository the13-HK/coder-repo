X = int(input())

target_list = []

for n in range(1, 10):
    for m in range(1, 10):
        target_list.append(n * m)

sum_list = [x for x in target_list if x != X]
print(sum(sum_list))