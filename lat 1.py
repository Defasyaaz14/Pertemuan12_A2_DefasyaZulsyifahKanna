import math

def input_koefisien():
    a = int(input('Masukkan a: '))
    b = int(input('Masukkan b: '))
    c = int(input('Masukkan c: '))
    return a, b, c

def hitung_diskriminan(a, b, c):
    return (b**2) - (4*a*c)

def temukan_akar(a, b, d):
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1, x2

def main():
    a, b, c = input_koefisien()
    d = hitung_diskriminan(a, b, c)

    if d >= 0:
        x1, x2 = temukan_akar(a, b, d)
        print('Solusinya adalah {0} dan {1}'.format(x1, x2))
    else:
        print('Tidak ada solusi real.')

if __name__ == "__main__":
    main()

