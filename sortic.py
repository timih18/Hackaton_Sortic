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


a = []
b = []
a_input = input()
while a_input != '!':
    a.append(int(a_input))
    a_input = input()
while len(a) > 1:
    while a[0] != minimum(a):
        ra(a)
        print('ra')
    b.append(a[0])
    print('pb')
    a = a[1:]
b.append(a[0])
print(b)
a = []
for i in b:
    a.append(i)
    print('pa')
print(a)
