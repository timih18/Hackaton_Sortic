# sa sb ss
def sab(a):
    if len(a) > 1:
        a[0], a[1] = a[1], a[0]
    return a


# pa pb
def pab(a, b):
    if len(a) > 0:
        b.append(a[0])
        b = b[-1:] + b[:-1]
        a = a[1:]
    return a, b


# rra rrb rrr
def rrab(a):
    a = a[-1:] + a[:-1]
    return a


# ra rb rr
def rab(a):
    a = a[1:] + a[:1]
    return a


a = [int(i) for i in input().split()]
b = []
comms = input().split()
for i in comms:
    if i == 'sa':
        sab(a)
    elif i == 'sb':
        sab(b)
    elif i == 'ss':
        sab(a)
        sab(b)
    elif i == 'pa':
        pab(b, a)
    elif i == 'pb':
        pab(a, b)
    elif i == 'ra':
        rab(a)
    elif i == 'rb':
        rab(b)
    elif i == 'rr':
        rab(a)
        rab(b)
    elif i == 'rra':
        rrab(a)
    elif i == 'rrb':
        rrab(b)
    elif i == 'rrr':
        rrab(a)
        rrab(b)
if a == a.sort():
    print('OK')
else:
    print('KO')
