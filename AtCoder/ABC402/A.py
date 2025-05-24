S=list(input())

Upper = []
for i in S:
    if i.isupper():
        Upper.append(i)

print(''.join(Upper))