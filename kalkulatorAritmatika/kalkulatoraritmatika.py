# -*- coding: utf-8 -*-
"""kalkulatorAritmatika.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pQ2BGkEilDME6prrI0u9npcRmzX3FrEQ
"""

import streamlit as st

# Judul dan pengantar
st.title("🔬 Virtual Lab Aritmatika")
st.write("Eksplorasi operasi aritmatika dasar: tambah, kurang, kali, dan bagi.")

# Input bilangan
a = st.number_input("Masukkan bilangan pertama (a):", value=0.0)
b = st.number_input("Masukkan bilangan kedua (b):", value=0.0)

# Pilihan operasi
operation = st.selectbox("Pilih operasi aritmatika:", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"])

# Proses dan output
st.subheader("🔍 Hasil Perhitungan")

if operation == "Tambah (+)":
    result = a + b
    st.success(f"Hasil: {a} + {b} = {result}")
elif operation == "Kurang (-)":
    result = a - b
    st.success(f"Hasil: {a} - {b} = {result}")
elif operation == "Kali (×)":
    result = a * b
    st.success(f"Hasil: {a} × {b} = {result}")
elif operation == "Bagi (÷)":
    if b != 0:
        result = a / b
        st.success(f"Hasil: {a} ÷ {b} = {result}")
    else:
        st.error("⚠️ Tidak dapat membagi dengan nol!")

# Catatan tambahan
st.markdown("---")
st.info("Gunakan lab ini untuk belajar operasi aritmatika secara interaktif. Cocok untuk siswa SD hingga SMP.")