a = input()
b = input()
for i in range(len(a)):
    if a[i] != b[i]:
        print("1",end= "")
    else:
        print("0",end="")
