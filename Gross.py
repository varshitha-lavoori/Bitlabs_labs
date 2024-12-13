def gross():
    basic_sal = int(input("Enter ur basic salary"))
    hra = 0
    da = 0
    if (basic_sal < 10000):
        hra = basic_sal * (67 /100)
        da = basic_sal * (73 /100)
    elif (basic_sal >=10000 and basic_sal <=20000):
        hra = basic_sal * (69 /100)
        da = basic_sal * (76 /100)
    else:
        hra = basic_sal * (73 /100)
        da = basic_sal * (89 /100)
    gs = hra + da + basic_sal
    print(gs)
gross()


