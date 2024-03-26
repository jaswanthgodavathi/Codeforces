import math
import sys

# Read function
def read():
    x, f = 0, 0
    ch = sys.stdin.read(1)
    while '0' > ch or ch > '9':
        f = ch == '-'
        ch = sys.stdin.read(1)
    while '0' <= ch and ch <= '9':
        x = x * 10 + ord(ch) - ord('0')
        ch = sys.stdin.read(1)
    return -x if f else x

# Main logic
for _ in range(read()):
    n = read()
    if n % 2 == 0:
        x = n // 2
        y = int(math.sqrt(x))
        if y * y == x:
            print("YES")
            continue
    if n % 4 == 0:
        x = n // 4
        y = int(math.sqrt(x))
        if y * y == x:
            print("YES")
            continue
    print("NO")
