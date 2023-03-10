def digital_root(n):
    suma = 0
    n = str(n)
    for i in n:
        suma+=int(i)
    print(suma)
    if suma < 10:
        return suma
    else:
        return digital_root(suma)
digital_root(12345)
