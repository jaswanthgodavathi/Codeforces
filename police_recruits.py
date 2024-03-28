a = int(input())
lst = list(map(int,input().split()))
s = 0 
count = 0 
for i in range(len(lst)):
    if lst[i] == -1 and s == 0:
        count+= 1 
    else:
        s += lst[i]
print(count)