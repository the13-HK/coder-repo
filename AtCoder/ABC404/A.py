import string

string_list = list(string.ascii_lowercase)
S = list(input())

for i in string_list:
    if i not in S:
        print(i)
        break