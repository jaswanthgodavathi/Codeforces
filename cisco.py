# a = list(input().split())
# print(len(a))


a = int(input())
b = bin(a)[2:]  # Convert to binary and remove the '0b' prefix
c = b[::-1]     # Reverse the binary string
if b == c:
    print("Yes")
else:
    print("No")