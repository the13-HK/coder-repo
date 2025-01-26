Q=int(input())
snake_queue=[0]
pop_num=0
for i in range(Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        snake_queue.append(snake_queue[-1] + query[1])
    elif query[0]==2:
        pop_num += 1
    else:
        print(snake_queue[query[1] + pop_num - 1] - snake_queue[pop_num])
