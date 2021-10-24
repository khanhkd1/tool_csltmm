import math


def inverse(a, p):
    u = a
    v = p
    x1 = 1
    x2 = 0
    while u != 1:
        q = math.floor(v / u)
        r = v - u * q
        x = x2 - x1 * q
        v = u
        u = r
        x2 = x1
        x1 = x
    return (x1 % p)


def GCD(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a


def tinhN(n):
    s = 1
    for i in range(len(n)):
        s = s * n[i]
    return s


def tinhNi(s, n):
    ni = []
    for i in range(len(n)):
        x = s // n[i]
        ni.append(x)
    return ni


def tinhM(ni, n):
    m = []
    for i in range(len(n)):
        x = inverse(ni[i], n[i])
        m.append(x)
    return m


def nghichdaocosox(arr, n):
    arrA = []
    for i in range(len(n)):
        y = inverse(arr[i], n[i])
        arrA.append(y)
    return arrA


def tinhlaia(arrA, a):
    arrB = []
    for i in range(len(a)):
        x = arrA[i] * a[i]
        arrB.append(x)
    return arrB


def phanduTH(a, s, ni, m):
    sum = 0
    for i in range(len(m)):
        sum += a[i] * ni[i] * m[i]
    return sum % s, s


def solve():
    print('''
1. Có hệ số
2. Không hệ số
    ''')
    a = []
    n = []
    choose = input("Nhập lựa chọn: ")
    if choose == 1:
        he_so = []
        for i in range(3):
            he_so.append(int(input(f"\tNhập hệ số thứ {i+1}: ")))
            a.append(int(input(f"\tNhập a{i+1}: ")))
            n.append(int(input(f"\tNhập n{i+1}: ")))
        arrA = nghichdaocosox(he_so, n)
        arrB = tinhlaia(arrA, a)
        s = tinhN(n)
        ni = tinhNi(s, n)
        m = tinhM(ni, n)
        a, b = phanduTH(arrB, s, ni, m)
        print('\tKết quả: x = {} mod {}'.format(a, b))
    else:
        for i in range(3):
            a.append(int(input(f"\tNhập a{i+1}: ")))
            n.append(int(input(f"\tNhập n{i+1}: ")))
        s = tinhN(n)
        ni = tinhNi(s, n)
        m = tinhM(ni, n)
        a, b = phanduTH(a, s, ni, m)
        print('\tx = {} mod {}'.format(a, b))
