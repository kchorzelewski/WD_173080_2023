list = []
while(True):
    x = input()
    if x.isdigit():
        list.append(x)
    print(list)
    if x == 'end':
        break
