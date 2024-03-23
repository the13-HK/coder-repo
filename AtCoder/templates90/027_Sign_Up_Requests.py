N = int(input())
input_list = [input() for _ in range(N)]
registered = set()

for i, v in enumerate(input_list):
    if v in registered:
        continue
    else:
        print(i+1)
        registered.add(v)