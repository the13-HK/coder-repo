N, M = map(int, input().split())
S_list = [input() for _ in range(N)]
T_list = [input() for _ in range(M)]

first_target = T_list[0]
for i in range(N - M + 1):
    line = S_list[i]
    result = []
    start = line.find(first_target)
    end   = line.rfind(first_target)
    if start == -1 or end == -1:
        continue
    elif start == end:
        result.append(start)
    else:
        for j in range(start, end + 1):
            if line[j] == first_target[0]:
                result.append(j)
    for r in result:
        for j in range(M):
            if S_list[i + j][r:r + M] != T_list[j]:
                break
            if j == M - 1:
                print(f"{i + 1} {r + 1}")
                exit()