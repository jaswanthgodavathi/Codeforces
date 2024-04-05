n = int(input())
arr = list(map(int,input().split()))
maxi = max(arr)
answer = sum(maxi - x for x in arr)
print(answer)
#made a small chng\\a