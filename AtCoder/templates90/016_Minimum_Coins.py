N = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort(reverse=True)

A = N // coin_list[0]
remain = N % coin_list[0]
ans = 9999

for i in range(A + 1):
    B = remain + i* coin_list[0] // coin_list[1]
    for j in range(B + 1):
        if N - (i*coin_list[0] + j*coin_list[1]) >= 0:
            check = (N - (i*coin_list[0] + j*coin_list[1])) % coin_list[2]
            if check == 0:
                ans = min(ans, i+j+(N - (i*coin_list[0] + j*coin_list[1])) // coin_list[2])
            else:
                continue
        else:
            break
print(ans)