def gen_key_Merkle_Hellman(n, M, W, daysieutang, hoanvi):
    arr = [''] * n
    for i in range(n):
        arr[i] = daysieutang[hoanvi[i] - 1]
    for i in range(n):
        arr[i] = arr[i] * W % M
    ke = arr
    kd = hoanvi, M, W, daysieutang
    return ke, kd


def encrypt_Merkle_Hellman(ke, m):
    c = 0
    for i in range(len(m)):
        if m[i] == "1":
            c += ke[i]
    return c


def decrypt_Merkle_Hellman(kd, c):
    hoanvi, M, W, daysieutang = kd
    d = c * pow(W, -1, M) % M
    # giải bài toán xếp balo
    S = d
    arr = []
    for i in range(len(daysieutang)):
        if S >= daysieutang[i]:
            arr.append('1')
            S = S - daysieutang[i]
        else:
            arr.append('0')
    a = [''] * len(arr)
    for i in range(len(arr)):
        a[i] = arr[hoanvi[i] - 1]
    return ''.join(a)


def solve():
    n = int(input('\tNhập n: '))
    M = int(input('\tNhập M: '))
    W = int(input('\tNhập W: '))
    day_sieu_tang = [int(i.strip()) for i in input("\tNhập dãy siêu tăng: ").split(',')]
    hoan_vi = [int(i.strip()) for i in input("\tNhập dãy hoán vị: ").split(',')]
    ke, kd = gen_key_Merkle_Hellman(n, M, W, day_sieu_tang, hoan_vi)
    print(f'\tKhoá công khai : {ke}')
    print(f'\tKhoá bí mật : {kd}')

    print("""
1. Mã hoá
2. Giải mã
""")
    choose = int(input("Chọn chức năng: "))
    if choose == 1:
        m = input("\tNhập bản tin m (bản rõ): ")
        c = encrypt_Merkle_Hellman(ke, m)
        print(f'\tbản mã : {c}(10)')
    else:
        c = int(input("\tNhập bản mã: "))
        m = decrypt_Merkle_Hellman(kd, c)
        print(f'\tbản rõ : {m}(2)')
