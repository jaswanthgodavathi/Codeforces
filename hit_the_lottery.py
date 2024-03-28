count = 0
a = int(input())
while a > 0:
    while a>=100:
        a = a-100
        count+=1 
    while a>= 20:
        a = a-20
        count+=1
    while a>=10:
        a = a-10
        count +=1 
    while a>=5:
        a = a-5
        count+=1 
    while a>=1:
        a = a-1 
        count+= 1
print(count)