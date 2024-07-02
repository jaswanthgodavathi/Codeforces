for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    print("YES" if sum(a)%2==1 or (any(ai%2==0 for ai in a) and any(ai%2==1 for ai in a)) else "NO")