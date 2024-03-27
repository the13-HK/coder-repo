from atcoder.lazysegtree import LazySegTree

w,n=map(int,input().split())
lst=[0]*w

def op(data1,data2):
  return max(data1,data2)

e=-1

def mapping(lazy_upper,data_lower):
  if lazy_upper==-1:
    return data_lower
  else:
    return lazy_upper

def composition(lazy_upper,lazy_lower):
  if lazy_upper==-1:
    return lazy_lower
  else:
    return lazy_upper

_id=-1

lazy_segtree=LazySegTree(op,e,mapping,composition,_id,lst)

for _ in range(n):
  l,r=map(int,input().split())
  l-=1
  max_height=lazy_segtree.prod(l,r)
  lazy_segtree.apply(l,r,max_height+1)
  print(max_height+1)
  