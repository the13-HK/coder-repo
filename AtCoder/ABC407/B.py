X, Y = map(int, input().split())

all = 36

pattern = [1, 2, 3, 4, 5, 6]

x_dict = {}
y_dict = {}

for p in pattern:
  for q in pattern:
    if x_dict.get(p + q) is None:
      x_dict[p + q] = [(p, q)]
    else:
      x_dict[p + q].append((p, q))
    if y_dict.get(abs(p - q)) is None:
      y_dict[abs(p - q)] = [(p, q)]
    else:
      y_dict[abs(p - q)].append((p, q))


fillment_pettern = set()
for i in range(X, 13):
  x_pattern = x_dict.get(i)
  for j in x_pattern:
    fillment_pettern.add(j)

for i in range(Y, 6):
  y_pattern = y_dict.get(i)
  for j in y_pattern:
    fillment_pettern.add(j)

print(len(fillment_pettern)/all)