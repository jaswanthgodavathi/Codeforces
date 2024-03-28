'''for _ in range(int(input())):
    a = int(input())
    lst = list(map(int, input().split()))
    result = all(x == lst[0] for x in lst)
    if result:
        print(-1)
    else:
        maximum = max(lst)
        flag = 0
        for i in range(a):
            if lst[i] == maximum:
                if i - 1 >= 0 and lst[i-1] < lst[i]:
                    print(i+1)
                    flag = 1
                    break
                if i + 1 < a and lst[i+1] < lst[i]: 
                    print(i+1)
                    flag = 1
                    break
for i in range(int(input())):
    a = int(input())
    b = input()
    if len(b)%3 == 0:
        for i in range(0,len(b),3):
            if b[i] == '1' and (b[i+1]=='1' or b[i+2] == '1'):
                b[i] = '1' 
                b[i+1] = '0'
                b[i+2] ='0'
            
    elif len(b)%3 == 1:
        for i in range(1,len(b),3):
            if b[i] == '1' and (b[i+1]=='1' or b[i+2] == '1'):
                b[i] = '1' 
                b[i+1] = '0'
                b[i+2] ='0'
        
    elif len(b)%3 == 2:
        for i in range(2,len(b),3):
            if b[i] == '1' and (b[i+1]=='1' or b[i+2] == '1'):
                b[i] = '1' 
                b[i+1] = '0'
                b[i+2] ='0'
            
    print(b)
'''
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    arr = []
    for i in s:
        arr += [i]
    act = 0
    for j in range(n-2):
        if arr[j]=='1':
            act = 1
            break
    if not act:
        print(s)
    else:
        print("0"*j + '1' + "0"*(n-j-1))
            
    
        
        
    
    


    
        
