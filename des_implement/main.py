import numpy as np
from function import ip, split_lo_ro, fiestel, list_keys, ip_inverse_index, transpose
import sys


def hex_to_bin(hex_value):
    if len(hex_value) > 16:
        print("Đầu vào là chuỗi 16 kí tự hexa")
        sys.exit()
    array_bin = []
    for i in range(len(hex_value)):
        array_bin += "{0:04b}".format(int(hex_value[i], 16)).strip(" ")
    return np.array(array_bin, dtype=int).reshape((8, 8))


def en_de_crypt(x, k, en_or_de):
    """

    :param x: string 16 character hex
    :param k:
    :return:
    """
    x = hex_to_bin(x)
    k = hex_to_bin(k)

    x0 = ip(x)

    l0, r0 = split_lo_ro(x0)

    keys = list_keys(k)

    for i in range(1, 17):
        print(f'\n### Vòng lặp thứ {i}')

        l_temp, r_temp = l0, r0
        l0 = r_temp
        if en_or_de >= 0:
            r0 = np.logical_xor(l_temp, fiestel(r_temp, keys[i - 1])).astype(int)
        else:
            r0 = np.logical_xor(l_temp, fiestel(r_temp, keys[16 - i])).astype(int)

        print(f'\tl({i}): {l0}')
        print(f'\tr({i}): {r0}')

    after_ip_inverse = transpose(
        np.concatenate((r0, l0), axis=0).reshape((8, 8)), ip_inverse_index()).flatten().tolist()
    return hex(int(''.join(str(i) for i in after_ip_inverse), 2)).replace('0x', '')


# print(f"\nBản mã: {en_de_crypt('00123456789abcde', '0133457799bbcdff', 1)}")
print(f"\nBản rõ: {en_de_crypt('1abff69d5a93e80b', '0133457799bbcdff', -1)}")
