N = int(input())
ans = [["?" for j in range(N)] for i in range(N)]

for i in range(N):
    j = N - i
    if i <= j:
        if i % 2 == 1:
            for k in range(i, j):
                for l in range(i, j):
                    ans[k][l] = "."
        else:
            for k in range(i, j):
                for l in range(i, j):
                    ans[k][l] = "#"

for i in range(N):
    print("".join(ans[i]))