# res[i][c] := i •¶Žš–ÚˆÈ~‚ÅÅ‰‚É•¶Žš c ‚ª“oê‚·‚é index
# ‘¶Ý‚µ‚È‚¢‚Æ‚«‚Í N
def calc_next(S):
    # •¶Žš—ñ S ‚Ì’·‚³
    N = len(S)

    # “š‚¦
    res = [[N] * 26 for _ in range(N + 1)]

    # Œã‚ë‚©‚çŒ©‚é
    for i in range(N - 1, -1, -1):
        # i + 1 •¶Žš–ÚˆÈ~‚ÌŒ‹‰Ê‚ðˆê’U i •¶Žš‚ÉƒRƒs[
        for j in range(26):
            res[i][j] = res[i + 1][j]

        # i •¶Žš–Ú‚Ìî•ñ‚ð”½‰f‚³‚¹‚é
        res[i][ord(S[i]) - ord('a')] = i

    # “š‚¦‚ð•Ô‚·
    return res

# “ü—Í
N, K = map(int, input().split())
S = input()

# ‘Oˆ—
res = ''
nex = calc_next(S)

# æÃ—~–@
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]

        # ‚¿‚á‚ñ‚Æ K •¶Žš‚ªì‚ê‚ê‚Î OK
        if N - k >= K - i:
            res += chr(ord('a') + ordc)
            j = k
            break
print(res)