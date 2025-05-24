S = list(input())

reversed_S = reversed(S)

count = 0
previous = 0
for i in reversed_S:
    i = int(i)
    if i > previous:
        count += i - previous
    elif i == previous:
        continue
    else:
        count += (10 + i) - previous
    previous = i

print(count + len(S))
    