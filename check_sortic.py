from colorama import Fore


def check_sorting(sp):
    for i in range(len(sp)-1):
        if sp[i] > sp[i+1]:
            return False
    return True


def sa_sb_ss(sp):
    if len(sp) > 1:
        sp[0], sp[1] = sp[1], sp[0]
    return sp


def pa_pb(sp1, sp2):
    if len(sp2) > 0:
        sp1.append(sp2[0])
        rra_rrb_rrr(sp1)
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
instruction = input()
instructions = []
while instruction != '!':
    instructions.append(instruction)
    instruction = input()
if not a:
    print(Fore.LIGHTRED_EX + 'empty list')
else:
    b = []
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
        if (i == 'ra' or i == 'rr') and len(a) > 0:
            ra_rb_rr(a)
        if (i == 'rb' or i == 'rr') and len(b) > 0:
            ra_rb_rr(b)
        if (i == 'rra' or i == 'rrr') and len(a) > 0:
            rra_rrb_rrr(a)
        if (i == 'rrb' or i == 'rrr') and len(b) > 0:
            rra_rrb_rrr(b)
    if check_sorting(a) and not b:
        print(Fore.GREEN + 'OK')
    else:
        print(Fore.RED + 'KO')
