# UAS

| Variable | Isi |
| -------- | --- |
| **Nama** | Thondy Autarliandi |
| **NIM** |  312310668 |
| **Kelas** | TI.23.A.6 |
| **Mata Kuliah** | Bahasa Pemrograman |
| **Dosen** | Agung Nugroho,S.Kom.,M.Kom |

## Projek uas untuk membuat sebuah program kasir pada sebuah kantin
- berikut adalah kode untuk menampilkan sebuah menu pada kasir
 kode tersebut menampilkan beberapa macam menu yang di jual 
```
menu = {
    "1": ["Nasi Goreng", 15000],
    "2": ["Soto", 9000],
    "3": ["Mie Ayam", 11000],
    "4": ["Es Teh Manis", 3000],
    "5": ["Es Jeruk", 4000],
    "6": ["Es Campur", 5000]
    }
```
- jika program diatas dijalankan makan outputnya sebagai berikut:

![SS 1](https://github.com/Thndyyy/UAS/assets/148066593/a9a2d649-ff6d-470f-837a-013b9260952c)

-  Inisialisasi Variabel
```
total_harga = 0
pesan = "Y"
```
- `total_harga = 0:` Variabel ini digunakan untuk menyimpan total harga dari seluruh pesanan yang akan dilakukan.
- `pesan = "Y":` Variabel ini digunakan untuk menyimpan input dari pengguna apakah masih ingin memesan lagi. Program akan terus melakukan looping selama input pengguna adalah "Y".
- Berikut kode sebagai proses pemesanan
```
while pesan.upper() == "Y":
    print("Daftar Menu:")
    for key, value in menu.items():
        print(key, value[0], "\tRp", value[1])
    pilihan = input("Masukkan pilihan menu (1/2/3/4/5/6): ")
    jumlah_pesan = int(input("Masukkan jumlah pesanan: "))
    harga = menu[pilihan][1] * jumlah_pesan
    total_harga += harga
    pesan = input("Ingin memesan lagi? (Y/N): ")
```
Kode ini dapat dianggap sebagai proses pemesanan, yang akan berlanjut hingga ketik "N" diterima. Setelah itu, program akan menghitung total harga, diskon, dan PPN, dan menampilkan struk pembayaran.
- jika program tersebut dijalankan maka outputnya sebagai berikut:

   ![SS 2](https://github.com/Thndyyy/UAS/assets/148066593/53e696c4-71b0-45da-b49b-031a078e13b4)

- Menghitung total harga dan menampilkan struk pembayaran
```
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
```
- Pada bagian kode tersebut, terdapat dua peran utama, yaitu menghitung total harga dan menampilkan struk pembayaran. Berikut adalah penjelasan masing-masing peran dalam kode tersebut:
### Menghitung Total Harga
- ``ppn = int(total_harga * 0.1):`` Menghitung pajak pertambahan nilai (PPN) sebesar 10% dari total harga.
- ``if jumlah_pesan >= 5:`` ... else: ...: Melakukan pengecekan apakah jumlah pesanan lebih dari atau sama dengan 5. Jika ya, maka akan diberikan diskon sebesar 20% dari total harga. Jika tidak, diskon akan diatur sebagai 0.
- ``total_harga = total_harga - diskon + ppn atau total_harga = total_harga + ppn:`` Menghitung total harga setelah diberikan diskon dan ditambahkan PPN.
### Menampilkan Struk Pembayaran
- ``print("Total harga: Rp", total_harga):`` Menampilkan total harga yang harus dibayar.
- ``print("Diskon: Rp", diskon):`` Menampilkan besaran diskon yang diberikan.
- ``print("PPN: Rp", ppn):`` Menampilkan besaran PPN yang harus dibayar.
- ``print("Total bayar: Rp", total_harga + ppn):`` Menampilkan total bayar yang sudah termasuk PPN.
Dengan demikian, bagian ini bertanggung jawab untuk menghitung total harga berdasarkan pesanan yang dibuat, serta menampilkan rincian pembayaran kepada pengguna.
- Jika program dijalankan maka outpunya sebagai berikut:

  ![SS 3](https://github.com/Thndyyy/UAS/assets/148066593/5a3029d3-e15d-466b-aea0-27612c0078a9)

- Berikut kode dalam bentuk gambar yang diambil melalui ekstensi ``Code Snap`` pada VsCode

 ![code SS](https://github.com/Thndyyy/UAS/assets/148066593/69590d34-c9cb-40cf-9fda-8111914304db)

### Sekian dari saya jika terdapat kesalahan kata dalam menjelaskan mohon dimaafkan dan doakan agar mendapatkan nilai UAS yang sempurna:)
  

