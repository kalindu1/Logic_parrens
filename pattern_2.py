ipt = input("type the number:- ")
ipt = int(ipt)

for i in range(ipt):
    temp = ipt-i
    for i in range(temp):
        print("*", end="")

    print()
