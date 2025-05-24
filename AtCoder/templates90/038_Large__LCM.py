A, B = map(int, input().split());

value = A * B
output = value
min = 2
max = value

while min <= (max - 1):
    if value % min == 0 :
        max = value // min
        output = 
    min += 1
    print(min, max , value)

if max > 10 ** 18:
    print('Large')
else:
    print(max)