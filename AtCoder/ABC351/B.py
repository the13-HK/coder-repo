N = int(input())
A_list = []
B_list = []
for i in range(N):
    A = input()
    A_list.append(A)
for i in range(N):
    B = input()
    B_list.append(B)

for i in range(N):
    if A_list[i] == B_list[i]:
        continue
    else:
        A = list(A_list[i])
        B = list(B_list[i])
        for j in range(N):
            if A[j] == B[j]:
                continue
            else:
                print(f"{i+1} {j+1}")