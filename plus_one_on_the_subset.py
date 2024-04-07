for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    print(max(lst) - min(lst))