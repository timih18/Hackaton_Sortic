from colorama import Fore


def check_sorting(sp):
    for i in range(len(sp)-1):
        if sp[i] > sp[i+1]:
            return False
    return True


def minimum(sp):
    mi_sp = sp[0]
    for i in sp:
        if i < mi_sp:
            mi_sp = i
    return mi_sp


def pa_pb(sp1, sp2):
    if len(sp2) > 0:
        sp1.append(sp2[0])
        rra_rrb_rrr(sp1)
    return sp1, sp2


def rra_rrb_rrr(sp):
    num = sp[-1]
    for i in range(len(sp), 0, -1):
        sp[i-1] = sp[i-2]
    sp[0] = num
    return sp


def ra(sp):
    num = sp[-1]
    for i in range(len(sp)):
        sp[i-1] = sp[i]
    sp[-2] = num
    return sp


a = [int(i) for i in input().split()]
if not a:
    print(Fore.RED + 'empty list')
elif check_sorting(a):
    print(Fore.GREEN + 'list already sorted')
else:
    b = []
    while not check_sorting(a):
        while a[0] != minimum(a):
            ra(a)
            print(Fore.BLUE + 'ra')
        b.append(a[0])
        a = a[1:]
        print(Fore.YELLOW + 'pb')
    for i in b:
        pa_pb(a, b)
        b = b[1:]
        print(Fore.CYAN + 'pa')
