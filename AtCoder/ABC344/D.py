T = input()
T_count = len(T)
N = int(input())
S = ""
max_list = []
string_bag = []
min_cost = -1
for i in range(N):
    list = input().split()
    max_list.append(int(list[0]))
    string_bag.append(list[1:])
dp = [[""]  * N] * N
cost = [[-1] * N] * N

for i in range(N):
    string_list = string_bag[i]
    for j in range(max_list[i] - 1):
        string = string_list[j]
        pre_string = dp[i][j-1]
        S = pre_string + string
        if T == S:
            cost[i][j] = cost[i][j-1] + 1
            break
        elif T.startswith(S):
            cost[i][j] = cost[i][j-1] + 1
            dp[i][j] = S
            continue
        else:
            cost[i][j] = cost[i][j-1]
            dp[i][j] = dp[i][j-1]

print(cost)