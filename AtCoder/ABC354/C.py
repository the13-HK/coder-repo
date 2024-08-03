N = int(input())
cards = [list(map(int, input().split())) + [i+1] for i in range(N)]
cards.sort(key=lambda x: x[0], reverse=True)
output = []
standard = cards[0][1]
for count in cards:
    if standard >= count[1]:
        standard = count[1]
        output.append(count[2])
        next
    else:
        next


output.sort()
print(len(output))
print(*sorted(output), end=" ")