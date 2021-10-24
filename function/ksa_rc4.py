
def solve():
    s = [i for i in range(0, 256)]
    j = 0
    t = [0] * 256
    t[0] = int(input("Nhập t[0]: "))
    t[1] = int(input("Nhập t[1]: "))
    for i in range(256):
        print(f'\ti = {i}')
        j = (j + s[i] + t[i]) % 256
        print(f'\tTrước khi swap: s[i]] = {s[i]}, s[j] = {s[j]}')
        s[i], s[j] = s[j], s[i]
        print(f'\tSau khi swap: s[i]] = {s[i]}, s[j] = {s[j]}')
