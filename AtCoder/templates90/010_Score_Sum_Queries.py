N = int(input())
class_1 = [0] * (N+1)
class_2 = [0] * (N+1)
for i in range(1, N+1):
    c, p = map(int, input().split())
    if c == 1:
        class_1[i] = class_1[i-1] + p
        class_2[i] = class_2[i-1]
    else:
        class_2[i] = class_2[i-1] + p
        class_1[i] = class_1[i-1]
Q = int(input())
output = []

for _ in range(Q):
    L ,R = map(int, input().split())
    print(str(class_1[R] - class_1[L-1])+" "+str(class_2[R] - class_2[L-1]))