# a,b = map(int,input().split())
# count = 0
# for i in range(a):
#     row = []
#     for j in range(a):
#         if (i+1)*(j+1) == b:
#             count += 1
# print(count)
a, b = map(int, input().split())
count = 0
for i in range(1, a + 1):
    if b % i == 0 and b // i <= a:
        count += 1
print(count)