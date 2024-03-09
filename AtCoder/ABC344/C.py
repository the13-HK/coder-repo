N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
L = int(input())
C = set(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

A_B = set([x + y for x in A for y in B ])

for x in X:
    flg = False
    for c in C:
        if (x - c) in A_B:
            flg = True
            break
    
    if flg:
        print("Yes")
    else:
        print("No")