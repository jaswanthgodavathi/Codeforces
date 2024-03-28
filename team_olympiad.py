from collections import Counter
a = int(input())
lst = list(map(int,input().split()))
ones = lst.count(1)
twos = lst.count(2)
threes = lst.count(3)
print(min(ones,twos,threes))
indexes_of_ones = [i for i, num in enumerate(lst) if num == 1]
indexes_of_twos = [i for i, num in enumerate(lst) if num == 2]
indexes_of_threes = [i for i, num in enumerate(lst) if num == 3]
for i in range(min(ones,twos,threes)):
    print(indexes_of_ones[i]+1,indexes_of_twos[i]+1,indexes_of_threes[i]+1)