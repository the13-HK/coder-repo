N=int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)

status=0
count = 0
for s in S:
    if s == "login":
        status = 1
    elif s == "logout":
        status = 0
    elif s == "private":
        if status == 0:
            count += 1
        else:
            continue
    elif s == "public":
        continue

print(count)
            