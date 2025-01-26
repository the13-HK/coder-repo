L, R = map(int, input().split())

def is_snake(n):
    nl = list(map(int, list(str(n))))
    for m in range(1, len(nl)):
        if nl[m] >=  nl[0]:
            return 0
    return 1

def cnt_snake(n):
    ret = 0
    nl = list(map(int, list(str(n))))
    # nそのものがスネーク数かどうか
    ret += is_snake(n)
    # nと同じ桁がスネーク数が何個あるか
    for k in range(1, nl[0]):
        ret += k ** (len(nl) - 1)
    # nより桁が小さいものがスネーク数が何個あるか
    for i in range(1, len(nl)):
        for j in range(1, 10):
            ret += j ** (i - 1)
    #  桁がxの桁と同じかつ、先頭桁の数字がxと同じもののスネーク数が何個あるか
    for l in range(1, len(nl)):
        if l > 1 and nl[l-1] >= nl[0]:
            break
        ret += min(nl[0], nl[l]) * (nl[0] ** (len(nl) - l - 1))
    return ret

print(cnt_snake(R) - cnt_snake(L - 1))