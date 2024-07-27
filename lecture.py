n, m = map(int, input().split())
t = {}
for _ in range(m):
    a, b = input().split()
    t[a] = b
result = []
x = input().split()
for i in range(len(x)):
    y = t.get(x[i], x[i])
    if len(y) < len(x[i]):
        result.append(y)
    else:
        result.append(x[i])
print(' '.join(result))
