no = int(input("Type a no."))
arr = []
i = 2
checker = 2
checkerChange = "False"
flag = 0
while len(arr) < no:
    # print('while1')
    while checker < i:
        # print('while2')
        if i % checker == 0:
            # print('flag add')
            flag = flag + 1
            checkerChange = "False"
            i = i + 1
            checker = 2
            break
        else:
            # print('checker add')
            checker = checker + 1
            checkerChange = "True"
    if i == checker:
        # print('checker change')
        flag = 0
        checkerChange = "False"
    if flag == 0 and checkerChange == "False":
        # print(f'append {i}' )
        arr.append(i)
        i = i + 1
        checker = 2
print(arr)
