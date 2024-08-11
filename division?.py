for i in range(int(input())):
    a = int(input())
    if a >= 1900:
        print('Division 1')
    elif a >= 1600 and a <=1899:
        print('Division 2')
    elif a >= 1400 and a <=1599:
        print('Division 3')
    else:
        print('Division 4')
    