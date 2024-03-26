a = input()
consecutive_count = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        consecutive_count += 1
        if consecutive_count >= 7:
            print("YES")
            break
    else:
        consecutive_count = 1  # Reset the consecutive count
else:
    print("NO")