N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(x:int):
    count = 0
    for a in A:
        count += x // a
    return count

start = 1
end = 10 ** 9

while start < end:
    mid = (start + end ) // 2
    numPrint = check(mid)
    if numPrint >= K:
        end = mid
    elif numPrint < K:
        start = mid + 1

print(start)