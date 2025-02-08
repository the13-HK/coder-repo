from collections import Counter
N = int(input())
kk = []
dd = []
sets = []

for _ in range(N):
    parts = list(map(int, input().split()))
    m_i = parts[0]
    elements = parts[1:]
    cnt = Counter(elements)
    dd.append(cnt)
    kk.append(m_i)
    sets.append(set(cnt.keys()))

max = 0
for i in range(N):
    Ki = sets[i]
    for j in range(i + 1, N):
        Kj = sets[j]
        if Ki.isdisjoint(Kj) == True:
            continue
        total = kk[i] * kk[j]
        count = 0
        count_i = dd[i]
        count_j = dd[j]
        if total == 0:
            continue
        if len(count_i) <= len(count_j):
            count = sum(i_val * count_j.get(k, 0) for k, i_val in count_i.items())
        else:
            count = sum(j_val * count_i.get(k, 0) for k, j_val in count_j.items())
        probability = count / total
        if probability > max:
            max = probability
                
print(max)