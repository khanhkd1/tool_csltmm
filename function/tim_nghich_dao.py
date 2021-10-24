def tim_nghich_dao():
    print('Tim nghich dao cua a mod m')

    a = int(input('a = '))
    b = int(input('m = '))
    a1 = a
    b1 = b
    q = 0
    r = 0
    x = 0
    y = 0
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
        # print('|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|%-7d|' %
        #     (q, r, x, y, a, b, x2, x1, y2, y1))

    d = a
    x = x2
    y = y2
    if (d == 1):
        print('{}^-1 = {} mod {}'.format(a1, x if x > 0 else x + b1, b1))
    else:
        print('Khong co nghich dao')
