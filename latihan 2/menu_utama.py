from bangun_datar.menu import menu
from bangun_datar.persegi import persegi
from bangun_datar.lingkaran import lingkaran
from bangun_datar.segitiga import segitiga

# Memanggil menu
menu()

# Meminta pilihan dari pengguna
pilihan = int(input("Pilih bentuk (1/2/3/4): "))

# Menangani pilihan pengguna
if pilihan == 1:
    persegi()
elif pilihan == 2:
    lingkaran()
elif pilihan == 3:
    segitiga()
elif pilihan == 4:
    exit()
else:
    print("Pilihan tidak valid")
