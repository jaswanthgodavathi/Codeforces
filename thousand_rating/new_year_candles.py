a,b = map(int,input().split())
count = 0
temp = 0
while a > 0:
    count += 1 
    temp += 1
    if temp == b:
        temp = 1
        count += 1
    a -= 1
print(count)