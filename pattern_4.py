# expected pattern

 # *
 # **
 # ***
 # ****
 # *****
 # ****
 # ***
 # **
 # *

ipt = input("enter the number :- ")
ipt = int(ipt)


if ipt % 2 == 0:
    half = int(ipt/2)
    for i in range(half):
        i+=1
        for j in range(i):
            print("*", end="")
        print()


    for b in range(half):
        num = ipt-half
        num = num-b
        for k in range(num):
            print("*", end="")

        print()

else:
    half = int(ipt/2)+1
    for i in range(half):
        i+=1
        for j in range(i):
            print("*", end="")
        print()


    for b in range(half):
        num = ipt-half
        num = num-b
        for k in range(num):
            print("*", end="")

        print()
