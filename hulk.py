a = int(input())
string = ""
for i in range(a-1):
    if i%2 == 0:
        string += "I hate that "
    if i%2 == 1:
        string += "I love that "
if a%2 == 0:
    string += "I love it "
if a%2 == 1:
    string += "I hate it "
print(string)
