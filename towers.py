from collections import Counter
a = int(input())
b = list(map(int,input().split()))
c = []
for i in range(len(b)):
    if b[i] not in c:
        c.append(b[i])
element_counts = Counter(b)
most_common_element, frequency = element_counts.most_common(1)[0]
print(frequency,len(c))