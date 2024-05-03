s = input()
start = 'a'
sum = 0
for i in range(len(s)):
    l1 = abs(ord(s[i]) - ord(start))
    l2 = 26 - abs(l1)
    sum += min(l1,l2)
    start = s[i]
print(sum)