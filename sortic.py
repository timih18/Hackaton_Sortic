from colorama import Fore


def minimum(a):
    mi_a = a[0]
    for i in a:
        if i < mi_a:
            mi_a = i
    return mi_a


def ra(a):
    b = a[-1]
    for i in range(len(a)):
        a[i-1] = a[i]
    a[-2] = b
    return a


a = [int(i) for i in input().split()]
b = []
while len(a) > 1:
    while a[0] != minimum(a):
        ra(a)
        print(Fore.BLUE + 'ra')
    b.append(a[0])
    print(Fore.BLUE + 'pb')
    a = a[1:]
b.append(a[0])
a = []
for i in b:
    a.append(i)
for i in range(len(b)-1):
    print(Fore.BLUE + 'pa')
