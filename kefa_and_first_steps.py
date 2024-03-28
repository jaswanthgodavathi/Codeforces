a = int(input())
l=1 
ml = 1 
lst = list(map(int,input().split()))
for i in range(1,a):
    if lst[i] >= lst[i-1]:
        l +=1 
        ml = max(ml,l)
    else:
        l = 1 
print(ml)