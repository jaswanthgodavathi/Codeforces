lst = list(map(int,input().split()))
s = input()
out = 0
for i in range(len(s)):
    out += lst[int(s[i]) - 1]
print(out)