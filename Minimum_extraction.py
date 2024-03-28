from bisect import bisect_left

FIO = lambda: None
FIO.input = input
FIO.print = print

FIO()

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n == 1:
        print(arr[0])
        continue
    
    arr.sort()
    
    if arr[0] < 0:
        mn_ele = arr[0]
        arr.pop(0)
        arr = [x - mn_ele for x in arr]
    
    ans, total = arr[0], 0
    
    for i in range(len(arr)):
        ans = max(ans, arr[i] - total)
        total += (arr[i] - total)
    
    print(ans)
