n, m = map(int,input().split())
matrix = []
flag = 0
for i in range(n):
    row = list(input().split())
    matrix.append(row)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'C'or  matrix[i][j] == 'M' or matrix[i][j] == 'Y':
            flag = 1 
            break
if flag == 1:
    print("#Color")
else:
    print("#Black&White")


    
