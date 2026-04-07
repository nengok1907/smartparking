import streamlit as st

st.set_page_config(page_title="Smart Parking PRO", layout="wide")

# =========================
# CSS
# =========================
st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 0;
}
.sub-title {
    color: #9aa4b2;
    margin-top: 0;
    margin-bottom: 20px;
    font-size: 18px;
}
.zone-title {
    font-size: 30px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 20px;
}
.road {
    background: linear-gradient(90deg, #2c3e50, #34495e);
    color: white;
    text-align: center;
    padding: 16px;
    border-radius: 12px;
    font-weight: 700;
    margin: 20px 0;
    letter-spacing: 1px;
}
.slot-card {
    border-radius: 16px;
    padding: 22px 10px;
    text-align: center;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    margin-bottom: 8px;
}
.slot-number {
    font-size: 24px;
    margin-bottom: 6px;
}
.slot-status {
    font-size: 20px;
}
.empty-card {
    background: linear-gradient(135deg, #4bff88, #27ae60);
    color: #0f172a;
}
.full-card {
    background: linear-gradient(135deg, #ff5a5a, #c0392b);
    color: white;
}
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    font-weight: 700;
    height: 42px;
}
.reset-wrap {
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# DATA
# =========================
FLOORS = 2
SLOTS = 10

if "parking" not in st.session_state:
    st.session_state.parking = [[0] * SLOTS for _ in range(FLOORS)]

# =========================
# FUNCTIONS
# =========================
def hitung():
    total = FLOORS * SLOTS
    terisi = sum(sum(area) for area in st.session_state.parking)
    kosong = total - terisi
    return total, terisi, kosong

def prediksi(kosong):
    if kosong == 0:
        return "PENUH", "#e74c3c"
    elif kosong <= 5:
        return "HAMPIR PENUH", "#f39c12"
    else:
        return "TERSEDIA", "#2ecc71"

def toggle_slot(area_index, slot_index):
    st.session_state.parking[area_index][slot_index] ^= 1

def render_slot(col, area_index, slot_index):
    status = st.session_state.parking[area_index][slot_index]

    if status == 1:
        card_class = "slot-card full-card"
        status_text = "TERISI"
        icon = "🔴"
        tombol = "Kosongkan"
    else:
        card_class = "slot-card empty-card"
        status_text = "KOSONG"
        icon = "🟢"
        tombol = "Isi Slot"

    col.markdown(
        f"""
        <div class="{card_class}">
            <div class="slot-number">{icon} Slot {slot_index + 1}</div>
            <div class="slot-status">{status_text}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if col.button(tombol, key=f"slot-{area_index}-{slot_index}"):
        toggle_slot(area_index, slot_index)
        st.rerun()

# =========================
# HEADER
# =========================
st.markdown('<div class="main-title">📍 Lokasi: Kawasan Braga - Bandung</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Smart Parking Dashboard</div>', unsafe_allow_html=True)

total, terisi, kosong = hitung()
status_prediksi = prediksi(kosong)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Slot", total)
m2.metric("Terisi", terisi)
m3.metric("Kosong", kosong)
status_prediksi, warna = prediksi(kosong)

m4.markdown(f"""
<div style="
    background: {warna};
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
    color: white;">
    AI Prediksi<br>{status_prediksi}
</div>
""", unsafe_allow_html=True)

st.divider()

# =========================
# AREA PARKING
# =========================
for area in range(FLOORS):
    st.markdown(f'<div class="zone-title">🏢 Kawasan A{area + 1}</div>', unsafe_allow_html=True)

    # Baris atas: slot 1-5
    cols_top = st.columns(5)
    for i in range(5):
        render_slot(cols_top[i], area, i)

    st.markdown('<div class="road">🚗 JALUR KENDARAAN</div>', unsafe_allow_html=True)

    # Baris bawah: slot 6-10
    cols_bottom = st.columns(5)
    for i in range(5, 10):
        render_slot(cols_bottom[i - 5], area, i)

    st.divider()

# =========================
# RESET
# =========================
st.markdown('<div class="reset-wrap"></div>', unsafe_allow_html=True)
if st.button("🔄 Reset Semua Slot"):
    st.session_state.parking = [[0] * SLOTS for _ in range(FLOORS)]
    st.rerun()