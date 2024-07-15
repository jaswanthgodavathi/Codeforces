for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    mini = min(a)
    maxa = max(a)
    min_index = a.index(mini)
    max_index = a.index(maxa)
    left_mini = min_index + 1 
    right_mini = n - min_index
    left_maxa = max_index + 1 
    right_maxa = n - max_index
    case1 = max(left_mini, left_maxa)
    case2 = max(right_mini,right_maxa)
    case3 = left_mini + right_maxa
    case4 = left_maxa + right_mini
    print(min(case1,case2,case3, case4))
    