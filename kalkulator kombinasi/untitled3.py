import streamlit as st
from itertools import product

st.set_page_config(page_title="Kombinasi Baju Visual", layout="wide")
st.title("👕 + 👗 Kombinasi Baju Laki-laki dan Perempuan")

# Gambar baju
baju_laki = {
    "L1": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Tshirt.svg/240px-Tshirt.svg.png",
    "L2": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Tshirt_red.svg/240px-Tshirt_red.svg.png",
    "L3": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Tshirt_blue.svg/240px-Tshirt_blue.svg.png"
}
baju_perempuan = {
    "P1": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Dress_icon.png/240px-Dress_icon.png",
    "P2": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Sundress_icon.png/240px-Sundress_icon.png",
    "P3": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Red_dress_icon.png/240px-Red_dress_icon.png"
}

# Pilihan interaktif
laki_selected = st.multiselect("Pilih baju laki-laki:", list(baju_laki.keys()), default=list(baju_laki.keys()))
perempuan_selected = st.multiselect("Pilih baju perempuan:", list(baju_perempuan.keys()), default=list(baju_perempuan.keys()))

if st.button("🎲 Tampilkan Kombinasi"):
    if not laki_selected or not perempuan_selected:
        st.warning("Pilih minimal satu dari kedua kategori.")
    else:
        kombinasi = list(product(laki_selected, perempuan_selected))
        st.success(f"Jumlah kombinasi: {len(kombinasi)}\n")

        st.markdown("### 🔍 Hasil Kombinasi Visual")
        for l, p in kombinasi:
            cols = st.columns([1, 1, 2])
            with cols[0]:
                st.image(baju_laki[l], caption=f"Laki‑laki: {l}", width=120)
            with cols[1]:
                st.image(baju_perempuan[p], caption=f"Perempuan: {p}", width=120)
            with cols[2]:
                st.markdown(f"👕 **{l}** + 👗 **{p}**")
            st.markdown("---")
