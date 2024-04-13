a = input()
count = 0
for i in range(len(a)):
    if a[i] == '4' or a[i] == '7':
        count += 1
if count == len(a):
    print("YES")
else:
    b = int(a)
    if b% 4 == 0 or b % 7 == 0 or b % 44 == 0 or b% 47 == 0 or b % 74 == 0 or b% 444 == 0 or b%447 == 0 or b % 474 == 0 or b% 477 == 0 or b % 777 == 0 or b % 774 == 0 or b% 744 ==0 : 
        print("YES")
    else:
        print("NO")