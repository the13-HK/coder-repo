N, H, W =  map(int, input().split())
list = [list(map(int, input().split())) for _ in range(N)]
sorted_list = sorted(list, key=lambda x: x[0]*x[1], reverse=True)
status = [[0 for _ in range(W)] for _ in range(H)]
dp = [[[0, 0] for _ in range(N)] for _ in range(N**3)]
dp[0][0] = [H, W]
flg = False
count = 0
remain_H = H
remain_W = W
while flg == False:
    dp[count][0] = [remain_H, remain_W]
    serach_list = sorted_list
    for i in range(1, N+1):
        tile = serach_list[i]
        remain_H = dp[count][i-1][0]
        remain_W = dp[count][i-1][1]
    if remain_H < 0 or remain_W < 0:
        next
        
    
    tile = sorted_list[count]
    target = sorted_list.filter(lambda x: x[0] * x[1] <= remain)