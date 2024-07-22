a = int(input())
lst = input()
out = 0
for i in range(len(lst)-2):
    if lst[i] == 'x' and lst[i+1] == 'x' and lst[i+2] == 'x':
        out += 1
print(out)
    