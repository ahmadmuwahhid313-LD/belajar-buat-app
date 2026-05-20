import streamlit as st

st.title("Program Pembelian Barang")

# Input
nama_barang = st.text_input("Masukkan nama barang")
harga_barang = st.number_input("Masukkan harga barang", min_value=0)
jumlah_barang = st.number_input("Masukkan jumlah barang", min_value=1)

# Tombol proses
if st.button("Hitung Total"):

    # Perhitungan
    total = harga_barang * jumlah_barang

    # Diskon
    if total >= 100000:
        diskon = total * 0.1
    else:
        diskon = 0

    bayar = total - diskon

    # Output
    st.subheader("Struk Pembelian")
    st.write("Nama Barang :", nama_barang)
    st.write("Harga Barang :", harga_barang)
    st.write("Jumlah Barang :", jumlah_barang)
    st.write("Total Harga :", total)
    st.write("Diskon :", diskon)
    st.write("Total Bayar :", bayar)
