from itertools import product

def isvalid(s):
    cnt = 0
    for c in s:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

n = int(input())

for s in product(['(', ')'], repeat=n):
    if isvalid(s):
        print(*s, sep='')