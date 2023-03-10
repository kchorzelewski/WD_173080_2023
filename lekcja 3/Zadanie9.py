def Zadanie9(a):
    spaces = int((a+(a-1))/2)+1
    spaces2 = -1
    spaces -= 1
    print(" "*spaces+"*")
    for i in range(a-1):
        spaces2 += 2
        spaces -= 1
        print(" "*spaces, end="")
        if i+1 == int(a/2):
            if a % 2 == 0:
                print("*", end="")
            print("*"*a)
            continue
        print("*", end="")
        print(" "*spaces2, end="")
        print("*")
Zadanie9(5)
