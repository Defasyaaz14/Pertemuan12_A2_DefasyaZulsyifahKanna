from bangun_datar.menu import menu

def lingkaran():
    print("Menghitung Luas Lingkaran")
    r = float(input("Masukkan Jari-Jari : "))
    luas = 3.14 * (r**2)
    print("Luas Lingkaran adalah ", luas)
    print()
    print("Coba lagi [Y/N]? ")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()