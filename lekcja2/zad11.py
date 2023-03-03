x = eval(input())
if x < 3 or x > 9:
    return 0
if x%2 == 0:
    x-=1
spaces = int(x/2)
for i in range(1, x, 2):
    print(" "*spaces,end="")
    spaces-=1
    print("o"*i)
print("o"*x)
for i in range(x-2,0,-2):
    spaces+=1
    print(" "*spaces,end="")
    print("o"*i)
