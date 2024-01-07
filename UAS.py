
menu = {
    "1": ["Nasi Goreng", 15000],
    "2": ["Soto", 9000],
    "3": ["Mie Ayam", 11000],
    "4": ["Es Teh Manis", 3000],
    "5": ["Es Jeruk", 4000],
    "6": ["Es Campur", 5000]
}


total_harga = 0
pesan = "Y"


while pesan.upper() == "Y":
    print("Daftar Menu:")
    for key, value in menu.items():
        print(key, value[0], "\tRp", value[1])
    pilihan = input("Masukkan pilihan menu (1/2/3/4/5/6): ")
    jumlah_pesan = int(input("Masukkan jumlah pesanan: "))
    harga = menu[pilihan][1] * jumlah_pesan
    total_harga += harga
    pesan = input("Ingin memesan lagi? (Y/N): ")


ppn = int(total_harga * 0.1)
if jumlah_pesan >= 5:
    diskon = int(total_harga * 0.2)
    total_harga = total_harga - diskon + ppn
else:
    diskon = 0
    total_harga = total_harga + ppn


print("Total harga: Rp", total_harga)
print("Diskon: Rp", diskon)
print("PPN: Rp", ppn)
print("Total bayar: Rp", total_harga + ppn)