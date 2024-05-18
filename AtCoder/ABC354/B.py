N = int(input())
T = 0
list = []
for i in range(N):
    s, c = input().split()
    T += int(c)
    list += [[s, int(c)]]

list.sort(key=lambda x: x[0])
winnner = T % N

print(list[winnner][0])
