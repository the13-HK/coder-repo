N, K = map(int, input().split())
S = input()

one_list = []

init_search = 0
count = 0

for r in range(N):
    if S[count] != S[r]:
        one_list.append(S[count:r])
        count = r
one_list.append(S[count:])

p = c = 0
for i, t in enumerate(one_list):
    if t[0] == '1':
        c += 1
    if c == K:
        p = i
        break

one_list[p], one_list[p-1] = one_list[p-1], one_list[p]
print(''.join(one_list))