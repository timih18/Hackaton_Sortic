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

for i in instructions:
    if i == 'sa' or i == 'ss':
        sa_sb_ss(a)
    if i == 'sb' or i == 'ss':
        sa_sb_ss(b)
    if i == 'pa':
        pa_pb(a, b)
        b = b[1:]
    if i == 'pb':
        pa_pb(b, a)
        a = a[1:]
    if i == 'ra' or i == 'rr':
        ra_rb_rr(a)
    if i == 'rb' or i == 'rr':
        ra_rb_rr(b)
    if i == 'rra' or i == 'rrr':
        rra_rrb_rrr(a)
    if i == 'rrb' or i == 'rrr':
        rra_rrb_rrr(b)
cnt = 0
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        cnt = 1
        break
if cnt == 0:
    print(Fore.GREEN + 'OK')
else:
    print(Fore.RED + 'KO')
