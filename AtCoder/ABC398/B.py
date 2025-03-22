A = list(map(int, input().split()))
set_A = set(A)
count_2 = []
count_3 = []
for i in set_A:
    c = A.count(i)
    if c == 2:
        count_2.append(i)
    elif c >= 3:
        count_3.append(i)

if (len(count_2) >= 1 and len(count_3) >= 1) or (len(count_3) >= 2):
    print("Yes")
else:
    print("No")