matrix = []
for i in range(5):
    row = []
    for j in range(5):
        value = int(input())
        if value == 1:
            flag = i 
            flag1 = j
        row.append(value)
    matrix.append(row)
print(flag, flag1)