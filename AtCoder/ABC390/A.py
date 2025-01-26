list_A = list(map(int, input().split()))
count = 0

for i in range(len(list_A)):
    if list_A[i] == i + 1:
        continue
    else:
        value = list_A.pop(i)
        list_A.insert(i + 1, value)
        count += 1
        if count != 1:
            break
print('Yes') if count == 1 else print('No')