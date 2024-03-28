
for i in range(int(input())):
    a = int(input())
    lst = []
    start = 1
    while len(lst) != a:
        if start%3 !=0 and start%10 != 3:
            lst.append(start)
            start+=1 
        else:
            start+=1
    print(lst[a-1])




