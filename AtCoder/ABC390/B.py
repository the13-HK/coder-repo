n = int(input())
a = list(map(int, input().split()))
flag=True

for i in range(n-2):
    if a[i]*a[i+2]!=a[i+1]*a[i+1]:
        flag=False
if flag:
    print("Yes")
else:
    print("No")