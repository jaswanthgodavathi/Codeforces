def main():
    t = int(input())
    for _ in range(t):
        x, y, a, b = map(int, input().split())

        if x > y:
            x, y = y, x

        ans1 = x*a + y*a
        z = y - x
        ans2 = z*a + x*b

        print(min(ans1, ans2))

if __name__ == "__main__":
    main()
