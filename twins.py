a = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
sum = 0 
count = 0
for i in range(len(lst)):
    sum += lst[i]
remanining = 0 
for i in range(len(lst)):
    if remanining <= sum:
        count+=1 
        sum -= lst[i]
        remanining+= lst[i]
print(count)

