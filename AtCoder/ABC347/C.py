N, A, B = map(int, input().split())
week = A + B
D=[int(i)%(A+B) for i in input().split()]
D.sort()
D.append(D[0]+week)

for i in range(N):
    diff = D[i+1] - D[i] - 1
    if diff >= B:
        print("Yes")
        break
else:
    print("No")