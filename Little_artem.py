for i in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = "B" * m
        matrix.append(row)
    for i in range(n):
        for j in range(m):
            if i == n - 1 and j == m - 1:
                matrix[i] = matrix[i][:j] + 'W'  
    for i in range(n):
        print(matrix[i])
