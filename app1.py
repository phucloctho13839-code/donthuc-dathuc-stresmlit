import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Toán 8 | Đơn thức – Đa thức",
    page_icon="📘",
    layout="wide"
)

# =========================
# CSS TÙY CHỈNH MÀU SẮC
# =========================
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}
h1, h2, h3 {
    color: #1f4bd8;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 2px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.highlight {
    color: #e63946;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TIÊU ĐỀ
# =========================
st.title("🏙️ THÀNH PHỐ ĐẠI SỐ")
st.subheader("📘 Chủ đề 1: ĐƠN THỨC – ĐA THỨC (Toán 8)")

st.markdown("---")

# =========================
# KHỞI ĐỘNG
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🚀 Khởi động")
    st.write("""
    Hãy tưởng tượng **Toán học là một thành phố**:
    - 🏠 Một ngôi nhà → **Đơn thức**
    - 🏘️ Một khu phố → **Đa thức**
    """)
    st.image("https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif", width=350)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# ĐƠN THỨC
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🏠 ĐƠN THỨC")
    st.write("""
    👉 **Đơn thức** là biểu thức chỉ gồm **một tích** của số và biến.
    """)
    st.code("3x   -2x²   5xy   7", language="python")

    st.info("""
    🔎 Cấu tạo:
    - Hệ số: số đứng trước
    - Phần biến: x, y, x²y³...
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# ĐA THỨC
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🏘️ ĐA THỨC")
    st.write("""
    👉 **Đa thức** là **tổng các đơn thức**.
    """)
    st.code("3x + 2y - 5\nx² + xy + y²", language="python")

    st.warning("""
    📌 Mỗi đơn thức trong đa thức gọi là **một số hạng**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# TƯƠNG TÁC – PHÂN LOẠI
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🎮 Trò chơi: Phân loại biểu thức")

    expr = st.text_input("Nhập một biểu thức đại số (ví dụ: 3x + 2y):")

    if expr:
        if "+" in expr or "-" in expr[1:]:
            st.success("✅ Đây là **ĐA THỨC** 🏘️")
        else:
            st.success("✅ Đây là **ĐƠN THỨC** 🏠")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# VẬN DỤNG THỰC TẾ
# =========================
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("🌍 Vận dụng thực tế")

    st.write("""
    Một học sinh mua:
    - x quyển vở (5000đ/quyển)
    - y cây bút (7000đ/cây)
    """)

    st.code("5000x + 7000y")

    st.success("👉 Đây là **đa thức**, mô tả một tình huống thực tế.")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# KẾT THÚC
# =========================
st.markdown("---")
st.markdown("### 🎯 Kết luận")
st.write("""
- 🏠 Đơn thức = một ngôi nhà
- 🏘️ Đa thức = một khu phố
- Toán học giúp **mô hình hóa cuộc sống**
""")
