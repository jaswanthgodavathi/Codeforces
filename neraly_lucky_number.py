a = input()
count = 0
flag = 0
for i in range(len(a)):
    if a[i] == '4' or a[i]== '7':
        count+=1
convert = str(count)
for i in range(len(convert)):
    if convert[i] == '4' or convert[i] == '7':
        continue
    else:
        flag = 1 
        break
if flag == 0:
    print("YES")
else:
    print("NO")