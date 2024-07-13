n, m = map(int, input().split())
outa = 0
outb = m
for i in range(n):
    temp1, temp2 = input().split()
    temp2 = int(temp2)
    if temp1 == '+':
        outb += temp2
    else:
        if outb - temp2 < 0:
            outa += 1
        else:
            outb -= temp2

print(outb, outa)
