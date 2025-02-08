N = int(input())
P = list(map(lambda i:int(i) - 1, input().split()))
Q = list(map(int, input().split()))
dict = dict(zip(Q, P))

for i in range(1, N + 1):
    print(Q[dict[i]], end = " ")