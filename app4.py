import streamlit as st
import random

# ===============================
# CẤU HÌNH TRANG
# ===============================
st.set_page_config(
    page_title="Toán 8 | Đơn thức – Đa thức",
    page_icon="📘",
    layout="wide"
)

# ===============================
# CSS TÙY BIẾN (NHẸ – ĐẸP)
# ===============================
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
h1, h2, h3 {
    color: #1f4bd8;
}
.box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.correct {
    color: green;
    font-weight: bold;
}
.wrong {
    color: red;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# TIÊU ĐỀ
# ===============================
st.title("📘 CHỦ ĐỀ 1: ĐƠN THỨC – ĐA THỨC (TOÁN 8)")
st.subheader("Học Toán bằng trải nghiệm – tương tác – công nghệ")

# ===============================
# THANH ĐIỀU HƯỚNG
# ===============================
menu = st.sidebar.radio(
    "📚 Chọn hoạt động học tập:",
    [
        "🏁 Khởi động",
        "📖 Kiến thức trọng tâm",
        "🔍 Phân loại biểu thức",
        "✏️ Luyện tập",
        "✅ Đánh giá nhanh"
    ]
)

# ===============================
# 1. KHỞI ĐỘNG
# ===============================
if menu == "🏁 Khởi động":
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.header("🏁 Khởi động")
    st.write("""
    Em hãy quan sát các biểu thức sau và suy nghĩ:
    - Biểu thức nào **chỉ có một hạng tử?**
    - Biểu thức nào **có nhiều hạng tử?**
    """)

    st.latex("3x^2")
    st.latex("2x + 5")
    st.latex("-x^3 + 2x - 1")

    st.info("👉 Hôm nay chúng ta sẽ khám phá cách phân loại các biểu thức này.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 2. KIẾN THỨC TRỌNG TÂM
# ===============================
elif menu == "📖 Kiến thức trọng tâm":
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.header("📖 Kiến thức trọng tâm")

    st.subheader("🔹 Đơn thức")
    st.write("""
    **Đơn thức** là biểu thức đại số gồm **một hạng tử**.
    Ví dụ:
    """)
    st.latex("5x")
    st.latex("-3x^2y")

    st.subheader("🔹 Đa thức")
    st.write("""
    **Đa thức** là tổng (hoặc hiệu) của **nhiều đơn thức**.
    Ví dụ:
    """)
    st.latex("x^2 + 2x + 1")
    st.latex("3x^3 - 2x + 4")

    st.warning("⚠️ Lưu ý: Mỗi hạng tử trong đa thức đều là một đơn thức.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 3. PHÂN LOẠI BIỂU THỨC
# ===============================
elif menu == "🔍 Phân loại biểu thức":
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.header("🔍 Phân loại biểu thức")

    expression = st.text_input("✍️ Nhập một biểu thức đại số (ví dụ: 2x+3):")

    if expression:
        if "+" in expression or "-" in expression[1:]:
            st.success("👉 Đây là **ĐA THỨC**")
        else:
            st.success("👉 Đây là **ĐƠN THỨC**")

    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 4. LUYỆN TẬP
# ===============================
elif menu == "✏️ Luyện tập":
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.header("✏️ Luyện tập nhanh")

    questions = [
        ("3x^2", "Đơn thức"),
        ("x^2 + 2x", "Đa thức"),
        ("-5xy", "Đơn thức"),
        ("x^3 - x + 1", "Đa thức")
    ]

    score = 0

    for i, (exp, ans) in enumerate(questions):
        choice = st.radio(
            f"Câu {i+1}: {exp} là?",
            ["Đơn thức", "Đa thức"],
            key=i
        )
        if choice == ans:
            score += 1

    st.write(f"🎯 Số câu đúng: **{score}/4**")
    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# 5. ĐÁNH GIÁ
# ===============================
elif menu == "✅ Đánh giá nhanh":
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.header("✅ Đánh giá – Phản hồi")

    feedback = st.text_area("💬 Em đã hiểu bài đến mức nào?")

    if st.button("📩 Gửi phản hồi"):
        st.success("Cảm ơn em! Giáo viên đã nhận được phản hồi.")

    st.info("👉 Giáo viên dựa vào kết quả để điều chỉnh bài dạy.")
    st.markdown('</div>', unsafe_allow_html=True)
