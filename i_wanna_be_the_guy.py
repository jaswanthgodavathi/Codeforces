a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))
set1 = set(b)
set2 = set(c)
if len(set1.union(set2)) == a:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")