def RealFloor(num):
    num = int(num)
    if num <= 0:
        return num
    else:
        if num <= 13:
            return num - 1
        else:
            return num - 2

pr = input("Real floor: ")
print(RealFloor(pr))