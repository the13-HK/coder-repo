N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()

output = 0
for n in range(N):
    output += abs(B_list[n] - A_list[n])
    
print(output)
