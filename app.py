import streamlit as st
import json
from streamlit_lottie import st_lottie

# =========================
# HÀM LOAD LOTTIE
# =========================
def load_lottie(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Toán 8 | Đơn thức – Đa thức",
    page_icon="📘",
    layout="wide"
)

# =========================
# CSS GIAO DIỆN
# =========================
st.markdown("""
<style>
body {background-color: #f4f6fb;}
h1, h2, h3 {color: #1f4bd8;}
.card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.step {
    background: linear-gradient(90deg,#1f4bd8,#6a82fb);
    color: white;
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD ANIMATION
# =========================
city_anim = load_lottie("assets/city.json")
math_anim = load_lottie("assets/algebra.json")

# =========================
# HEADER
# =========================
st.title("🏙️ THÀNH PHỐ ĐẠI SỐ")
st.subheader("Chủ đề 1: ĐƠN THỨC – ĐA THỨC | Toán 8")

st_lottie(city_anim, height=280)

# =========================
# DASHBOARD TIẾN TRÌNH
# =========================
st.markdown("## 🧭 Tiến trình tiết học")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Khởi động", "5 phút")
c2.metric("Khám phá", "20 phút")
c3.metric("Luyện tập", "10 phút")
c4.metric("Vận dụng", "10 phút")

# =========================
# KHỞI ĐỘNG
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🚀 Khởi động</div>", unsafe_allow_html=True)
    st.write("""
    - 🏠 Một ngôi nhà → **Đơn thức**
    - 🏘️ Một khu phố → **Đa thức**
    """)
    st_lottie(math_anim, height=220)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# KIẾN THỨC
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>📘 Kiến thức trọng tâm</div>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🏠 Đơn thức", "🏘️ Đa thức"])

    with tab1:
        st.write("**Đơn thức** là biểu thức chỉ gồm *một tích* của số và biến.")
        st.code("3x   -2x²   5xy   7")

    with tab2:
        st.write("**Đa thức** là *tổng các đơn thức*.")
        st.code("3x + 2y - 5\nx² + xy + y²")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# TRÒ CHƠI TƯƠNG TÁC
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🎮 Trò chơi: Phân loại nhanh</div>", unsafe_allow_html=True)

    expr = st.text_input("Nhập biểu thức (VD: 3x+2y):")

    if expr:
        if "+" in expr or "-" in expr[1:]:
            st.success("🏘️ Đây là **ĐA THỨC**")
        else:
            st.success("🏠 Đây là **ĐƠN THỨC**")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# QUIZ TỰ ĐÁNH GIÁ
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>📝 Quiz tự đánh giá</div>", unsafe_allow_html=True)

    score = 0

    q1 = st.radio("1️⃣ Biểu thức nào là đơn thức?",
                  ["3x + 2", "5xy", "x + y"])
    if q1 == "5xy":
        score += 1

    q2 = st.radio("2️⃣ Đa thức là:",
                  ["Một tích", "Một tổng các đơn thức", "Một số"])
    if q2 == "Một tổng các đơn thức":
        score += 1

    if st.button("📊 Xem kết quả"):
        st.success(f"🎉 Bạn đạt {score}/2 điểm")
        if score == 2:
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# VẬN DỤNG
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🌍 Vận dụng thực tế</div>", unsafe_allow_html=True)

    st.write("""
    Mua:
    - x quyển vở (5000đ)
    - y cây bút (7000đ)
    """)

    st.code("5000x + 7000y")
    st.info("👉 Đây là **đa thức**, mô hình hóa tình huống thực.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("🎯 **Kết luận:** Đơn thức = nhà, Đa thức = khu phố. Toán học giúp mô tả thế giới!")
