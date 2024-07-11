for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    s = sum(lst)
    print(s-a if s>= 1 else 1)
    