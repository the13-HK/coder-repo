N, K = map(int, input().split())
list = [0] * (N + 1)

for i in range(2, N+1):
    if list[i]:continue
    for j in range(i,N+1,i):
        list[j]+=1

res=0
for i in range(len(list)):
  if list[i]>=K:
    res+=1
print(res)