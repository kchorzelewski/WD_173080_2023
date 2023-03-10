a = ['a', 'b', 'c', 'd']
def dodaj_znak(a):
    for i in range(len(a)):
        a[i] = a[i]+"!"
    return a
dodaj_znak(a)

def dodaj_znak2(a):
    b = []
    for i in a:
        b.append(i+"!")
    return b
dodaj_znak2(a)
