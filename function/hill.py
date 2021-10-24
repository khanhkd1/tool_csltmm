import re


def input_text_k():
    en_de = input("\tNhập chức năng (en-de): ")
    text = input("\tNhập bản rõ hoặc bản mã: ")
    print("\tNhập khoá")
    a_11 = int(input("\t\tNhập phần tử a11: "))
    a_12 = int(input("\t\tNhập phần tử a12: "))
    a_21 = int(input("\t\tNhập phần tử a21: "))
    a_22 = int(input("\t\tNhập phần tử a22: "))

    return en_de, text, [[a_11, a_12], [a_21, a_22]]


def inversion(p, a):
    for i in range(p):
        chia = (a * i - 1) / p
        if chia == int(chia):
            return i


def en_decrypt(en_de, text, B):
    if en_de == 'de':
        detA, detA1 = det_a(B)
        B = [[(B[1][1] * detA1) % 26, (-B[0][1] * detA1) % 26],
             [(-B[1][0] * detA1) % 26, (B[0][0] * detA1) % 26]]

    subString = re.findall('\w{2}', text)
    ct = []
    for i in subString:
        x = [ord(i[0]) - ord('a'), ord(i[1]) - ord('a')]
        result = [chr((x[0] * B[0][0] + x[1] * B[1][0]) %
                      26 + ord('a')), chr((x[0] * B[0][1] + x[1] * B[1][1]) % 26 + ord('a'))]
        ct.append(''.join(result))
    return str(''.join(ct))


def det_a(B):
    detA = (B[0][0] * B[1][1] - B[0][1] * B[1][0]) % 26
    detA1 = inversion(26, detA)
    return detA, detA1


def find_key(plain_text, cipher_text):
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    B = [[i, j],
                         [k, l]]
                    try:
                        detA, detA1 = det_a(B)
                        B1 = [[(B[1][1] * detA1) % 26, (-B[0][1] * detA1) % 26],
                              [(-B[1][0] * detA1) % 26, (B[0][0] * detA1) % 26]]
                        if en_decrypt('en', plain_text, B) == cipher_text:
                            return B
                            print(B)
                    except:
                        continue
    return None
