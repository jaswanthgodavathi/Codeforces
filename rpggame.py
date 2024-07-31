# n = int(input())
# exp = int(input())
# lst = []
# for i in range(n):
#     val = int(input())
#     lst.append(val)
# bonus = []
# for i in range(n):
#     bon = int(input())
#     bonus.append(bon)
# count = 0
# for i in range(n):
#     if exp >= lst[i]:
#         count += 1 
#         exp += bonus[i]
#         print(exp)
# print(count)

# n = int(input())
# exp = int(input())

# monsters = []
# for i in range(n):
#     power = int(input())
#     monsters.append((power, 0))  # Initializing bonus as 0 for now

# for i in range(n):
#     bonus = int(input())
#     monsters[i] = (monsters[i][0], bonus)  # Adding bonus to the respective monster

# # Sort monsters by their power requirement
# monsters.sort()

# count = 0
# for power, bonus in monsters:
#     if exp >= power:
#         count += 1
#         exp += bonus
#     else:
#         break

# print(count)

a = input()
b = input()
seta = set(a)
setb = set(b)
temp = list(seta)
temp1 = list(setb)
strri = ''.join(temp)
strri2 = ''.join(temp1)
print(strri)
print(strri2)
print(strri - strri2)


