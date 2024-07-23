t = int(input())
for case in [input().strip() for _ in range(t)]:
    col, row = case[0], case[1]
    print(" ".join(f"{col}{r}" for r in "12345678" if r != row) + " " + " ".join(f"{c}{row}" for c in "abcdefgh" if c != col))