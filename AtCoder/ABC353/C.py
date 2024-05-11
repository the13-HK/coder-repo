N = int(input())
A = list(map(lambda x: int(x) % 10**8, input().split()))

def function(A):
    if len(A) == 1:
        return 0
    else:
        count = 0
        init = A[0]
        value += init * N - sum([i >= 10**8 - init for i in A[1:] ]) * 10**8
        return count + function(A[1:])      

print(function(A))