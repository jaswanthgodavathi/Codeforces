for i in range(int(input())):
    a = int(input())
    lst = list(map(int,input().split()))
    seta = set(lst)
    print(len(seta))