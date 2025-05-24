N = int(input())

S = []
for _ in range(N):
    s = list(input())
    S.append(s)

T = []
for _ in range(N):
    t = list(input())
    T.append(t)

def right_rot90(S):
  return list(zip(*S[::-1]))
def count_diff(S,T):
  return sum([1 for si,ti in zip(S,T) for sij,tij in zip(si,ti) if sij!=tij])

ans = 10**9

for rot_count in range(4):
  ans = min(ans, count_diff(S,T)+rot_count)
  S = right_rot90(S)
  
print(ans)