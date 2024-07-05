for i in range(int(input())):
    a = input()
    suma , sumb, sumc = 0,0,0
    for i in range(len(a)):
        if a[i] == 'A':
            suma += 1
        elif a[i] == 'B':
            sumb += 1 
        elif a[i] == 'C':
            sumc += 1 
    if suma+sumc == sumb:
        print("YES")
    else:
        print("NO")