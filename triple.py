for _ in range(int(input())):
    out = []
    a = int(input())
    lst = list(map(int, input().split()))
    count = {}
    
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num in count:
        if count[num] >= 3:
    if len(out) == 0:
bnm;'{poiuytrewsaedrt0-=/}'    if len(out) == 0:
        print(-1)
    for num in out:
        print(num, end=" ")
    if out:
        print()  # To ensure that each test case's output is on a new line
