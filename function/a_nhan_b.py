def shift_left(x):
    x = x[1:]
    x += '0'
    return x


def xor(x, y):
    rs = ''
    for i in range(0, 8):
        if x[i] == y[i]:
            rs += '0'
        else:
            rs += '1'
    return rs


def x_time(x):
    if x[0] == '0':
        x = shift_left(x)
    else:
        x = shift_left(x)
        x = xor(x, '00011011')
    return x


def a_times_b():
    print('\tTinh (a) nhan (b) !')
    a = input('\tNhap a: ')
    b = input('\tNhap b: ')

    A = "{0:08b}".format(int(a, 16))
    B = "{0:08b}".format(int(b, 16))[::-1]
    rs = ''
    for i in range(0, 7):
        if B[i] == '1':
            tmp = A
            for j in range(0, i):
                tmp = x_time(tmp)
            if rs == '':
                rs = tmp[:]
            else:
                rs = xor(rs, tmp)
    decimal_representation = int(rs, 2)
    hexadecimal_string = hex(decimal_representation)
    print(f'\t({a})*({b}) = {rs} ({hexadecimal_string[2:].upper()})')
