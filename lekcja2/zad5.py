a = eval(input())
b = eval(input())
c = eval(input())
if(a>0 and a<=10):
    if(a>b or b>c):
        print("liczba znajduje się w przedziale (0, 10> oraz a>b lub b>c")
    else:
        print("liczba znajduje się w przedziale (0, 10> oraz a<=b lub b<=c")
else:
    print("liczba nie znajduje się w przedziale (0, 10> oraz a<=b lub b<=c")
