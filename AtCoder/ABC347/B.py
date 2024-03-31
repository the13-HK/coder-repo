S = input()
set_S = set(S)
set_S.add(S)
dict_S = {}

for i in range(2, len(S)):
    for j in range(len(S) - i + 1):
        set_S.add(S[j:i+j])
print(len(set_S))