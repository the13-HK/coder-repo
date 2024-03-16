S = input()
if S.count('>') == 1 and S.count('<') == 1:
    if S == '<'*S.count('<') + '='*S.count('=') + '>'*S.count('>'):
        print('Yes')
    else:
        print('No')
else:
    print('No')