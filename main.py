from function.cipher import Cipher
from function import hill
from function.a_nhan_b import a_times_b
from function.euclide_mo_rong import euclid_mo_rong
from function import phan_du_trung_hoa
from function import xep_ba_lo
from function import merkle_hellman
from function import elliptic
from function import thang_du_blum
from function import tim_nghich_dao
from function import log
from function import ksa_rc4
from function import z_n

cipher = Cipher()

while True:
    print('''
1. Mã Cipher    2. Mã Hill    3. Tính A nhân B (hệ hexa)    4. Euclide mở rộng
5. Phần dư Trung Hoa    6. Xếp ba lô trên dãy siêu tăng    7. Merkle Hellman
8. Đường cong Elliptic    11. Thặng dư Blum
12. Tìm nghịch đảo    13. Tìm log_a(b) trên Z*n    14. KSA_RC4
15. Zn (cấp ptu, ptu sinh, thang du bac 2)
    
20. Thoát
''')

    choose = int(input('Chọn chức năng: '))
    if choose == 1:
        text = input("\tNhập bản rõ hoặc bản mã: ")
        k = int(input("\tNhập khoá k: "))
        cipher.show_result(text, k)

    elif choose == 2:
        print('''
        1. Mã hoá, giải mã
        2. Tìm khoá k
        ''')
        choose = int(input('Chọn chức năng: '))
        if choose == 1:
            en_de, text, k = hill.input_text_k()
            print(f'\tKết quả: {hill.en_decrypt(en_de, text, k)}')
        else:
            plain_text = input("\tNhập bản rõ: ")
            cipher_text = input("\tNhập bản mã: ")
            print(f'\t{hill.find_key(plain_text, cipher_text)}')

    elif choose == 3:
        a_times_b()

    elif choose == 4:
        euclid_mo_rong()

    elif choose == 5:
        phan_du_trung_hoa.solve()

    elif choose == 6:
        xep_ba_lo.solve()

    elif choose == 7:
        merkle_hellman.solve()

    elif choose == 8:
        elliptic.solve()

    elif choose == 11:
        thang_du_blum.solve()

    elif choose == 12:
        tim_nghich_dao.tim_nghich_dao()

    elif choose == 13:
        log.solve()

    elif choose == 14:
        ksa_rc4.solve()

    elif choose == 15:
        z_n.solve()

    elif choose == 20:
        break
