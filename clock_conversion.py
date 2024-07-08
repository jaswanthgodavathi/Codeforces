for i in range(int(input())):
    a, b = map(str, input().split(':'))
    cona = int(a)
    conb = int(b)
    if cona == 0:
        print(f"12:{b.zfill(2)} AM")
    elif cona == 12:
        print(f"12:{b.zfill(2)} PM")
    elif cona > 12:
        print(f"{str(cona - 12).zfill(2)}:{b.zfill(2)} PM")
    else:
        print(f"{a.zfill(2)}:{b.zfill(2)} AM")
