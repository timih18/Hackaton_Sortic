from colorama import Fore


def minimum(sp):
    mi_sp = sp[0]
    for i in sp:
        if i < mi_sp:
            mi_sp = i
    return mi_sp


def ra(sp):
    num = sp[-1]
    for i in range(len(sp)):
        sp[i-1] = sp[i]
    sp[-2] = num
    return sp


a = input().split()
if a == []:
    print('empty list')
else:
    b = []
    while len(a) > 1:
        while a[0] != minimum(a):
            ra(a)
            print(Fore.BLUE + 'ra')
        b.append(a[0])
        print(Fore.YELLOW + 'pb')
        a = a[1:]
    b.append(a[0])
    a = []
    for i in b:
        a.append(i)
    for i in range(len(b)-1):
        print(Fore.CYAN + 'pa')
