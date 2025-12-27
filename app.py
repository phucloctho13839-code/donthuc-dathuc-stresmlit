import streamlit as st
import json
from streamlit_lottie import st_lottie

# =========================
# LOAD LOTTIE
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
# CSS
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
st.subheader("CHỦ ĐỀ 1 – ĐƠN THỨC & ĐA THỨC | TOÁN 8")
st_lottie(city_anim, height=280)

# =========================
# TIẾN TRÌNH
# =========================
st.markdown("## 🧭 Tiến trình học tập")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Khởi động", "5 phút")
c2.metric("Khám phá", "15 phút")
c3.metric("Luyện tập", "10 phút")
c4.metric("Vận dụng – ĐG", "15 phút")

# =========================
# PHẦN 1: KHỞI ĐỘNG
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🚀 PHẦN 1. KHỞI ĐỘNG</div>", unsafe_allow_html=True)

    expr = st.text_input("Nhập một biểu thức đại số:")

    if expr:
        if "+" in expr or "-" in expr[1:]:
            st.success("🏘️ Bạn đang ở **KHU PHỐ – ĐA THỨC**")
        else:
            st.success("🏠 Bạn đang ở **NGÔI NHÀ – ĐƠN THỨC**")

    st_lottie(math_anim, height=200)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PHẦN 1: KHÁM PHÁ
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🔍 PHẦN 1. KHÁM PHÁ KIẾN THỨC</div>", unsafe_allow_html=True)

    expr2 = st.text_input("Nhập biểu thức để phân tích:")

    if expr2:
        terms = expr2.replace("-", "+-").split("+")
        st.write("🔎 Các thành phần:")
        for t in terms:
            if t.strip():
                st.code(t.strip())

    st.info("👉 Từ các thành phần trên, HS tự rút ra khái niệm đơn thức – đa thức.")
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# AI MÔ PHỎNG
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🤖 TRỢ LÝ ĐẠI SỐ (AI MÔ PHỎNG)</div>", unsafe_allow_html=True)

    ai_expr = st.text_input("Hỏi AI về biểu thức của bạn:")

    if ai_expr:
        if "+" in ai_expr:
            st.info(f"Biểu thức {ai_expr} là **đa thức** vì gồm nhiều đơn thức cộng lại.")
        else:
            st.info(f"Biểu thức {ai_expr} là **đơn thức** vì chỉ có một tích.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# LUYỆN TẬP
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🎮 LUYỆN TẬP – PHÂN LOẠI NHANH</div>", unsafe_allow_html=True)

    test_expr = st.text_input("Nhập biểu thức bất kỳ:")

    if test_expr:
        if "+" in test_expr or "-" in test_expr[1:]:
            st.success("👉 ĐA THỨC")
        else:
            st.success("👉 ĐƠN THỨC")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# ĐÁNH GIÁ
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>📝 ĐÁNH GIÁ QUÁ TRÌNH</div>", unsafe_allow_html=True)

    score = 0
    q1 = st.radio("1️⃣ Biểu thức nào là đơn thức?", ["3x+1", "5xy", "x+y"])
    if q1 == "5xy":
        score += 1

    q2 = st.radio("2️⃣ Biểu thức nào là đa thức?", ["7", "2x", "x+3"])
    if q2 == "x+3":
        score += 1

    if st.button("📊 Xem kết quả"):
        st.success(f"🎯 Điểm của bạn: {score}/2")
        if score == 2:
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# SẢN PHẨM HỌC TẬP
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🎨 SẢN PHẨM HỌC TẬP</div>", unsafe_allow_html=True)

    name = st.text_input("Tên học sinh:")
    context = st.text_area("Mô tả tình huống thực tế:")
    expr_prod = st.text_input("Biểu thức đại số mô tả:")

    if st.button("📥 Nộp sản phẩm"):
        st.success("✅ Đã nộp sản phẩm!")
        st.write(f"👤 {name}")
        st.write(context)
        st.code(expr_prod)

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PHẢN TƯ
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='step'>🧠 PHẢN TƯ HỌC TẬP</div>", unsafe_allow_html=True)

    reflection = st.text_area("Hôm nay em học được gì?")
    if reflection:
        st.info("🌱 Cảm ơn em – phản tư giúp học sâu hơn!")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("📘 **Kết luận:** Đơn thức là nền móng – Đa thức là cấu trúc của đại số.")
