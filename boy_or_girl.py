a = input()
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
if len(b)%2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')