def max_a(a):
    max_a = a[0]
    for i in a:
        if i > max_a:
            max_a = i
    return max_a


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
    while a[0] != max_a(a):
        ra(a)
        print('ra')
    b.append(a[0])
    print('pa')
    a = a[1:]
b.append(a[0])
print(b)
