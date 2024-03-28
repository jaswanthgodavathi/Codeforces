lst = list(map(int,input().split()))
operation = 0
while len(lst) != 1:
    lst.sort()
    operation += lst[0] + lst[1]
    a = lst[0] +lst[1]
    lst.append(a)
    lst.pop(0)
    lst.pop(1)
    print(lst)
print(operation)