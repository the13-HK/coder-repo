end = False
list = []
while end == False:
    n = int(input())
    if n == 0:
        end = True
        list.insert(0, n)
        break
    else:
        list.insert(0, n)
        
print(*list, sep='\n')