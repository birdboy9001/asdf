def spreadNumber(n):
    stri = "1"
    for x in range(2, int(n) + 1):
        stri = stri + ", " + str(x)
    print("[" + stri + "]")
spreadNumber(input("Number "))