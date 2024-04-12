a  = input()
temp = "hello"
cou = 0
for i in range(len(a)):
    if a[i] == temp[cou]:
        cou += 1
    if cou == 5:
        break
if cou == 5:
    print("YES")
else:
    print("NO")