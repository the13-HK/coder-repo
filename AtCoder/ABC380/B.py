S = input().split("|")[1:-1]
A = map(lambda x: len(x), S)
print(*A)