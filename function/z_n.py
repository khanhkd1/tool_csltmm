from math import gcd
from random import randint


def findR_S(n):
    dem = 0
    n = n - 1
    while n % 2 == 0:
        dem += 1
        n /= 2
    return dem, int(n)


def modular_pow(a, k, n):
    binary = bin(k)[2:]
    b = 1
    if k == 0:
        return b
    A = a
    if binary[-1] == '1':
        b = a

    for i in range(1, len(binary)):
        A = (A ** 2) % n

        if binary[-1 - i] == '1':
            b = A * b % n
    return b


def miller_rabin(n, t=5):
    s, r = findR_S(n)
    arrRand = []
    for i in range(1, t + 1):
        a = randint(2, n - 2)
        while a in arrRand:
            a = randint(2, n - 2)
        arrRand.append(a)
        if gcd(a, n) != 1:
            return False
        else:
            y = modular_pow(a, r, n)
            if y != 1 and y != n - 1:
                j = 1
                while j <= s - 1 and y != n - 1:
                    y = (y ** 2) % n
                    if y == 1:
                        return False
                    j += 1
                if y != n - 1:
                    return False
            return True


def pollard_rho2(n, c=5):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5
    elif n % 7 == 0:
        return 7
    elif miller_rabin(n):
        return n
    a = 2
    b = 2
    while True:
        a = (a ** 2 + c) % n
        b = (b ** 2 + c) % n
        b = (b ** 2 + c) % n
        d = gcd(abs(a - b), n)
        if 1 < d and d < n and miller_rabin(d):
            return d
        if d == n:
            return pollard_rho2(n, c - 1)


def analyze(n):
    coSo = list()
    soMu = list()

    while n != 1:

        dem = 0
        i = pollard_rho2(n)
        while n % i == 0 and i != 1:
            dem += 1
            n //= i
        if dem > 0:
            coSo.append(i)
            soMu.append(dem)
    return coSo, soMu


def phi_n(n):
    coSo, soMu = analyze(n)
    result = n
    for i in coSo:
        result *= (1 - (1 / i))

    return result


def tim_z_sao(n):
    return [i for i in range(1, n) if gcd(i, n) == 1]


def ord(n):
    a = tim_z_sao(n)
    ordArray = []
    for i in a:
        for j in range(1, len(a) + 1):
            if (i ** j) % n == 1:
                ordArray.append(j)
                break

    return a, ordArray


def solve():
    n = int(input("\tNhập n: "))
    a, ordArray = ord(n)

    # print('{}'.format(a))

    print(f'\tCấp phần tử')
    for i in range(len(a)):
        print(f'({a[i]}, {ordArray[i]})', sep=' ')

    # print('|Zn| Cap cua cac phan tu la:')
    # print('{}'.format(ordArray))

    print('Cac phan tu sinh la:')
    pts = [a[i] for i in range(len(a)) if ordArray[i] == len(a)]
    print('{}'.format(pts))

    print('Qn Tap thang du bac 2: ')
    tapthangdu = [(i ** 2) % n for i in a if (i ** 2) % n in a]
    print(sorted(set(tapthangdu)))

