from colorama import Fore


def sa_sb_ss(sp):
    if len(sp) > 1:
        sp[0], sp[1] = sp[1], sp[0]
    return sp


def pa_pb(sp1, sp2):
    if len(sp2) > 0:
        sp1.append(sp2[0])
        rra_rrb_rrr(sp1)
        # --------------------------------pop-------------------------------- #
        sp2 = sp2.pop(0)
    return sp1, sp2


def ra_rb_rr(sp):
    num = sp[-1]
    for i in range(len(sp)):
        sp[i-1] = sp[i]
    sp[-2] = num
    return a


def rra_rrb_rrr(sp):
    num = sp[-1]
    for i in range(len(sp), 0, -1):
        sp[i-1] = sp[i-2]
    sp[0] = num
    return sp


a = [int(i) for i in input().split()]
b = []
instructions = input().split()
for i in instructions:
    if i == 'sa' or i == 'ss':
        sa_sb_ss(a)
    elif i == 'sb' or i == 'ss':
        sa_sb_ss(b)
    elif i == 'pa':
        pa_pb(a, b)
    elif i == 'pb':
        pa_pb(b, a)
    elif i == 'ra' or i == 'rr':
        ra_rb_rr(a)
    elif i == 'rb' or i == 'rr':
        ra_rb_rr(b)
    elif i == 'rra' or i == 'rrr':
        rra_rrb_rrr(a)
    elif i == 'rrb' or i == 'rrr':
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
