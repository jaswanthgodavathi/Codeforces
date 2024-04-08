lst = [1,11,111,1111,2,22,222,2222,3,33,333,3333,4,44,444,4444,5,55,555,5555,6,66,666,6666,7,77,777,7777,8,88,888,8888,9,99,999,9999]
for i in range(int(input())):
    a = int(input())
    check = 0
    for i in range(len(lst)):
        if lst[i] == a:
            flag = i
    count = 0
    for i in range(flag+1):
        count += len(str(lst[i]))
    print(count)