lst = list(map(int,input().split()))
dist = set(lst)
count = len(dist)
print(len(lst) - count)