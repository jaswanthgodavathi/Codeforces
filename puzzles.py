'''n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
least = lst[n-1] - lst[0]
for i in range(1,m-n+1):
    if lst[i+n-1] - lst[i] < least:
        least = lst[i+n-1] - lst[i]
print(least)'''
