Q = int(input())

queue = []
count=0
for q in range(Q):
    query_list = list(map(int, input().split()))
    if query_list[0] == 1:
        queue.append(query_list[1]) 
    else:
        print(queue[count])
        count += 1
    