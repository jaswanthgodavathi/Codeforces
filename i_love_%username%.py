a = int(input())
countp = 0
countn = 0
lst = list(map(int,input().split()))
for i in range(1,len(lst)):
    if a[i] > a[i-1]:
        countp += 1