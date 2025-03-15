S = list(input())
count = 0
flg = True
for i in range(len(S)):
    if i % 2 == 1:
        if S[i] == "i" and flg == True:
            count += 1
            flg = False
        elif S[i] == "o" and flg == False:
            count += 1
            flg = True
    else:
        if S[i] == "o" and flg == True:
            count += 1
            flg = False
        elif S[i] == "i" and flg == False:
            count += 1
            flg = True
if (len(S) + count) % 2 == 1:
    count += 1
print(count)

