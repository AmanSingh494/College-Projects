no = int(input("Give a number"))
i = 2
flag = 0
while i <= no / 2:
    if no % i == 0:
        flag = flag + 1
        print("given no. is not prime")
        break
    i = i + 1

if flag == 0:
    print("No. is prime")
else:
    pass
