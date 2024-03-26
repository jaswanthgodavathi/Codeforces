a = int(input())
sum = 0
count = 0
count0 = 0
lst = list(map(int,input().split()))
#lst.sort(reverse=True)
for i in range(len(lst)):
    #sum += lst[i]
    if lst[i] == 5:
        count += 1
    else:
        count0 += 1
if count0 == 0: 
    print(-1)
elif count >= 9:
    temp = count//9
    count = temp*9
    result = '5' * count + '0' * count0
    print(result)
else:
    print(0)
