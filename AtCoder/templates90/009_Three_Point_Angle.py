import sys, math
from collections import defaultdict, deque

def dist(j, k, mod):
  return (k - j)%mod

def undist(j, k, mod):
  return (k + j)%mod

def deg_normal(deg):
  if deg < 0:
    deg += 360
  if deg > 180:
    deg = 360 - deg
  return deg

def main(f):
  N = int(f.readline())
  P = [None]
  for n in range(1, N+1):
    x, y = map(int, f.readline().split())
    P.append((x, y))

####
  result = 0
  for i in range(1, N+1): # O(N)
    O = P[i] 
    deg_list = []

    for j in range(1, N+1): # O(N)
      if j == i:
        continue
      x = P[j][0] - O[0]
      y = P[j][1] - O[1]
      cos = x / math.sqrt(x*x + y*y)
      deg = math.degrees(math.acos(cos))
      if y < 0:
        deg += (180-deg)*2
      deg_list.append(deg)
    deg_list.sort() # O(N*log N)

    for j in range(len(deg_list)): # O(N)
      mod = len(deg_list)
      high = -1 #j - 1
      low = j + 1
      high = dist(j, high, mod)
      low = dist(j, low, mod)
      while high > low: # O(log N)
        m = low + (high-low) // 2
        deg = deg_list[undist(j, m, mod)] - deg_list[j]
        deg_r = deg_list[undist(j, m+1, mod)] - deg_list[j]
        deg = deg_normal(deg)
        deg_r = deg_normal(deg_r)
        if deg_r > deg:
          low = m + 1
        else:
          high = m
      max_deg = deg_list[undist(j, low, mod)] - deg_list[j]
      max_deg = deg_normal(max_deg)
      if max_deg > result:
        result = max_deg

  print(result)

main(sys.stdin)