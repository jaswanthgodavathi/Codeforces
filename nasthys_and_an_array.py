
a = int(input())
b = list(map(int,input().split()))
i = 0
while i < len(b):
    if b[i] == 0:
        b.pop(i)
    else:
        if b.count(b[i]) > 1:
            b.pop(i)
        else:
            i += 1

print(len(b))
