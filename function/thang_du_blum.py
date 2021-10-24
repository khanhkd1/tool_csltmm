def nhanbinhphuongcolap(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    if k & 1 == 1:
        b = a
    for i in range(1, len(bin(k)) - 2):
        A = (A ** 2) % n
        if (k >> i) & 1 == 1:
            b = (A * b) % n
    return b


def extendEuclide(a, b):
    if b == 0:
        d = a
        x = 1
        y = 0
        return (d, x, y)
    else:
        x2 = 1
        x1 = 0
        y2 = 0
        y1 = 1
        while b > 0:
            q = a // b
            r = a - q * b
            x = x2 - q * x1
            y = y2 - q * y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
        d = a
        x = x2
        y = y2
        return (d, x, y)


def timthangdu(n, p, q, c):
    d, x, y = extendEuclide(p, q)
    a = x % n
    b = y % n
    p1 = (p + 1) // 4
    q1 = (q + 1) // 4
    r = nhanbinhphuongcolap(c, p1, p)
    s = nhanbinhphuongcolap(c, q1, q)
    x = (a * p * s + b * q * r) % n
    y = (a * p * s - b * q * r) % n
    return (x, -x % n, y, -y % n)


def solve():
    print('\tTìm thặng dư của c mod p*q')
    p = int(input("\tNhập p: "))
    q = int(input("\tNhập q: "))
    c = int(input("\tNhập c: "))
    print(f'\t{timthangdu(p*q, p, q, c)}')

