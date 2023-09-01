def maximum(a, b, c):
    if a > b and a > c:
        print(a, " is maximum")
    elif b > a and b > c:
        print(b, " is maximum")
    else:
        print(c, " is maximum")


no1 = int(input("Enter First No"))
no2 = int(input("Enter second No"))
no3 = int(input("Enter third No"))
maximum(no1, no2, no3)
