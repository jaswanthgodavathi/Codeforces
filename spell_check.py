for _ in range(int(input())):
    b = int(input())
    a = input()
    flag = 0
    a = list(a)  # Convert the input string to a list of characters
    a.sort()  # Sort the list of characters
    a = ''.join(a)  # Join the sorted characters to form a string

    if len(a) == 5:
        if a[1] == 'i' and a[2] == 'm' and a[3] == 'r' and a[4] == 'u' and a[0] == 'T':
            print("Yes")
            flag = 1

    if flag == 0:
        print("No")
