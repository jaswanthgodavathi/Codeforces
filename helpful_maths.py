a = input()
lst = []

if len(a) == 1:
    print(a)
else:
    for i in range(0, len(a), 2):
        lst.append(int(a[i]))
    lst.sort()
print('+'.join(map(str, lst)))
