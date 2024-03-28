a = int(input())
l = 0
r = 0
u = 0
d = 0
str = input()
for i in range(len(str)):
    if str[i] == 'L':
        l+=1 
    if str[i] == 'R':
        r+=1
    if str[i] == 'U':
        u+=1
    if str[i] == 'D':
        d+=1
temp1 = min(l,r)
temp2 = min(u,d)
print(2*temp1 + 2*temp2)
