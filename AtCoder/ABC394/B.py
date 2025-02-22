N = int(input())
S = []
for _ in range(N):
    i = input()
    S.append([len(i), i])

S = sorted(S)
print(''.join([x[1] for x in S]))