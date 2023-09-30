temp = 0
win = 0
for i in range(int(input())):
    c = int(input())
    for j in range(c):
        a,b = map(int,input().split())
        if a <=10:
            if b > temp:
                temp = b 
                win = j+1
    print(win)
