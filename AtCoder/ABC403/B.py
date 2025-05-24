T = input()
U = input()

for i in range(len(T) - len(U) + 1):
    ok = True
    for j in range(len(U)):
        if T[i + j] != "?" and T[i + j] != U[j]:
            ok = False
            break
    if ok:
        print("Yes")
        exit()
print("No")