s = input()
t = input()
pos = 0
for char in t:
    if char == s[pos]:
        pos += 1 
    if pos == len(s):
        break
print(pos + 1)

