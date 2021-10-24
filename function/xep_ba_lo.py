def xep_ba_lo(arr, s, n):
    v = []
    for i in range(n - 1, -1, -1):
        if s >= arr[i]:
            a = 1
            v.append(a)
            s = s - arr[i]
        else:
            a = 0
            v.append(a)
    return list(reversed(v))


def solve():
    s = int(input("\tNhập số nguyên S: "))
    arr = [int(i.strip()) for i in input("Nhập dãy số nguyên: ").split(',')]
    print(f'\t{xep_ba_lo(arr, s, len(arr))}')
