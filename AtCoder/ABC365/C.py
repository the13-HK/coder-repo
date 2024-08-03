N, M = map(int, input().split())
A = list(map(int, input().split()))

if M >= sum(A):
    print('infinite')
else:
    set_A = sorted(set(A))
    min_x = 0
    max_x = len(set_A) - 1 
    # print("set_A:", set_A)
    # print("min_x:", min_x)
    # print("max_x:", max_x)
    
    while True:
        search = set_A[( max_x + min_x ) // 2]
        # print("search:", search)
        above = list(filter(lambda x: x > search, A))
        below = list(filter(lambda x: x <= search, A))
        amount = search * len(above) + sum(below)
        # print(above)
        # print(below)
        # print(amount)
        
        if amount > M:
            max_x = set_A.index(search)
        else:
            min_x = set_A.index(search)
        # print("set_A:", set_A)
        # print("min_x:", min_x)
        # print("max_x:", max_x)
        if max_x - min_x <= 1:
            output = set_A[min_x]
            print(output)
            break 
        
        