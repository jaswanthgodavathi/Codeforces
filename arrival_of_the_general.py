n = int(input())
max_value = 0
min_value = 1000
max_index = 0
min_index = 0
x = list(map(int,input().split()))
for i in range(len(x)):
    
    
    if x[i] > max_value:
        max_index = i
        max_value = x[i]

    if x[i] <= min_value:
        min_index = i
        min_value = x[i]

if max_index > min_index:
    print((max_index - 1) + (n - min_index) - 1)
else:
    print((max_index - 1) + (n - min_index))
