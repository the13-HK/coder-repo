N=int(input())
A=list(map(int, input().split()))
B=list(map(int,input().split()))

ans=[0] * N
ans[0] = 0
ans[1] = A[0]

for i in range(2, N):
    ans[i] = min(ans[i - 2] + B[i - 2] , ans[i - 1] + A[i - 1])

return_value = N
list = [N]
while return_value > 0:
    if ans[return_value - 2] == ans[return_value - 1] - A[return_value - 2]:
        list.append(return_value - 1)
        return_value -= 1
    else:
        list.append(return_value - 2)
        return_value -= 2
list.pop()
list.reverse()

print(len(list))   
print(*list)