def Zadanie4(a1=1, r=1, ile=10):
    suma = a1
    for i in range(ile-1):
        a1+=r
        suma += a1
    return suma
Zadanie4()
