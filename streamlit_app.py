# Program Sederhana Pembelian Barang

print("=== PROGRAM PEMBELIAN BARANG ===")

# Input data barang
nama_barang = input("Masukkan nama barang : ")
harga_barang = int(input("Masukkan harga barang : "))
jumlah_barang = int(input("Masukkan jumlah barang : "))

# Perhitungan total
total = harga_barang * jumlah_barang

# Diskon sederhana
if total >= 100000:
    diskon = total * 0.1
else:
    diskon = 0

# Total akhir
bayar = total - diskon

# Output
print("\n=== STRUK PEMBELIAN ===")
print("Nama Barang   :", nama_barang)
print("Harga Barang  :", harga_barang)
print("Jumlah Barang :", jumlah_barang)
print("Total Harga   :", total)
print("Diskon        :", diskon)
print("Total Bayar   :", bayar)
