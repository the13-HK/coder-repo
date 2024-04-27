H, W = map(int, input().split())
S = []
commands = [(0, 1), (1, 0), (-1, 0), (0, -1)]
flex = [[0] * W for _ in range(H)]
history = [[0] * W for _ in range(H)]
for _ in range(H):
    s = input()
    S.append(s) 

for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            flex[h][w] = 0
        else:
            for command in commands:
                if h + command[0] < 0 or w + command[1] < 0 or h + command[0] > H or w + command[1] > W:
                    continue
                else:
                    try:
                        if S[h + command[0]][w + command[1]] == ".":
                            flex[h][w] += 1
                    except:
                        None
                        
def search (h, w, history, flex):
    if S[h][w] == "#":
        return 0
    else:
        if flex[h][w] == 1:
            return 0
        else:
            if history[h][w] > 1:
                return history[h][w]
            else:
                for command in commands:
                    if h + command[0] < 0 or w + command[1] < 0 or h + command[0] > H or w + command[1] > W:
                        history[h][w] += 0
                    else:
                        try:
                            history[h][w] += search(h + command[0], w + command[1], history, flex)
                        except:
                            history[h][w] += 0
                return history[h][w]

max = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        else:
            if history[h][w] == 0:
                history[h][w] = search(h, w, history, flex)
                if history[h][w] > max:
                    max = history[h][w]


print(max)