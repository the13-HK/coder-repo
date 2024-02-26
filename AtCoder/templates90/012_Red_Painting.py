import sys
input = lambda: sys.stdin.readline().rstrip()

# ‘½”{’·®”‚Ì§ŒÀ‰ğœ
# sys.set_int_max_str_digits(0)

# Ä‹A‚¨‚Ü‚¶‚È‚¢
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
# Ä‹AãŒÀ
sys.setrecursionlimit(10**7)

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

H, W = map(int, input().split())
D = [[0] * W for _ in range(H)]
uf = UnionFind(H * W)
Q = int(input())
for _ in range(Q):
    q = input().split()
    t = int(q[0])
    if t == 1:
        r, c = int(q[1]) - 1, int(q[2]) - 1
        D[r][c] = 1
        if c + 1 < W and D[r][c + 1] == 1:
            uf.union(r * W + c, r * W + c + 1)
        if r + 1 < H and D[r + 1][c] == 1:
            uf.union(r * W + c, (r + 1) * W + c)
        if c - 1 >= 0 and D[r][c - 1] == 1:
            uf.union(r * W + c, r * W + c - 1)
        if r - 1 >= 0 and D[r - 1][c] == 1:
            uf.union(r * W + c, (r - 1) * W + c)

    elif t == 2:
        ra, ca, rb, cb = int(q[1]) - 1, int(q[2]) - 1, int(q[3]) - 1, int(q[4]) - 1
        if D[ra][ca] == 1 and D[rb][cb] == 1 and uf.same(ra * W + ca, rb * W + cb):
            print('Yes')
        else:
            print('No')
