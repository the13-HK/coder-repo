H = int(input())

i = 0
h = 2 ** i

while H >= h:
    i += 1
    h += 2 ** i

print(i+1)