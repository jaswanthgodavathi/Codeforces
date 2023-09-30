a = int(input())
b = input()
counta = 0
countd = 0
for i in range(len(b)):
    if b[i] == 'A':
        counta += 1 
    else:
        countd +=1 
if counta>countd:
    print("Anton")
elif countd>counta:
    print("Danik")
else:
    print("Friendship")