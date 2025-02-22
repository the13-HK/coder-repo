import re 
S = input()
target_regrex = 'W{1,}A'
match_list = set(re.findall(target_regrex, S))
max_match = max(match_list, key=len)
W_len = len(max_match)
for match in range(W_len):
    S = re.sub('WA', 'AC', S)
print(S)
