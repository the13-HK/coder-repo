def solve(queue):
    while len(queue) > 1:
        a = queue.pop(-1)
        b = queue.pop(-1)
        if a == b:
            queue.append(a+1)
            continue
        else:
            queue.append(b)
            queue.append(a)
            break
    return queue

N = int(input())
A = list(map(int, input().split()))
queue = []

for n in A:
    queue.append(n)
    solve(queue)
print(len(queue))