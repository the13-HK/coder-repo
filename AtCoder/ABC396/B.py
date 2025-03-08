Q = int(input())
query_list = [ list(map(int, input().split())) for _ in range(Q) ] 
card = [0] * 100

for query in query_list:
    type = query[0]
    if type == 1:
        card.append(query[1])
    elif type == 2:
        print(card.pop(-1))