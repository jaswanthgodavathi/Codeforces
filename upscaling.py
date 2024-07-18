# for i in range(int(input())):
#     a = int(input())
#     b = 2*a
#     for i in range(b):
#         count = 0
#         for j in range(b//2):
#             if count != 0:
#                 if i%2 == 0:
#                     print("##", end = "")
#                 else:
#                     print("..", end = "")
#             else:
#                 if i%2 == 0:
#                     print("##", end = "")
#                 else:
#                     print("..", end = "")    
#         count += 1
#         if count == 1:
#             count = 0
#         print()

for i in range(int(input())):
    a = int(input())
    count = 0
    temp = 0
    for i in range(a*2):
        for j in range(a):
            if count%2 == 0:
                if j%2 == 0:
                    print("##", end = "")
                else:
                    print("..", end = "")
            else:
                if j%2 == 0:
                    print("..",end = "")
                else:
                    print("##", end = "")
        temp += 1
        if temp == 2:
            count += 1 
            temp = 0
        print()