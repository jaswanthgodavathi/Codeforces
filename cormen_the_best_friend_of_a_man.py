n,k = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
for i in range(1,len(lst)):
    if lst[i-1] + lst[i] < k:
        count += k - (lst[i]+lst[i-1])
        lst[i] += k - (lst[i]+lst[i-1])
print(count)
print(' '.join(map(str, lst)))