import streamlit as st
import google.generativeai as genai

# ===============================
# CẤU HÌNH TRANG
# ===============================
st.set_page_config(
    page_title="Toán 8 | Đơn thức – Đa thức",
    page_icon="📘",
    layout="centered"
)

# ===============================
# CẤU HÌNH GEMINI AI
# ===============================
# ⚠️ THAY BẰNG API KEY CỦA BẠN
genai.configure(api_key="AIzaSyDP7ppzyxvN62ZZv8u2QkplnX68moAO0yU")
model = genai.GenerativeModel("gemini-pro")

# ===============================
# CSS TRANG TRÍ
# ===============================
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.box {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.title {
    text-align: center;
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# TIÊU ĐỀ
# ===============================
st.markdown("<h1 class='title'>📘 CHỦ ĐỀ 1: ĐƠN THỨC – ĐA THỨC (TOÁN 8)</h1>", unsafe_allow_html=True)

# ===============================
# MENU
# ===============================
menu = st.sidebar.radio(
    "📌 Chọn nội dung học",
    [
        "🏁 Giới thiệu",
        "📘 Lý thuyết",
        "🧠 Nhận diện đơn thức – đa thức",
        "✍️ Luyện tập",
        "📝 Kiểm tra nhanh",
        "🤖 Trợ giảng AI (Tự học ở nhà)"
    ]
)

# ===============================
# NỘI DUNG 1: GIỚI THIỆU
# ===============================
if menu == "🏁 Giới thiệu":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("🎯 Mục tiêu bài học")
    st.write("""
    - Nhận biết được đơn thức và đa thức  
    - Phân biệt các biểu thức đại số  
    - Vận dụng kiến thức vào bài tập cơ bản  
    """)

    st.subheader("💡 Hình thức học tập")
    st.write("""
    - Học tương tác qua web app  
    - Tự khám phá – luyện tập – đánh giá  
    - Có trợ giảng AI hỗ trợ học ở nhà  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NỘI DUNG 2: LÝ THUYẾT
# ===============================
elif menu == "📘 Lý thuyết":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("📌 Đơn thức")
    st.write("""
    - Là biểu thức đại số chỉ gồm **một hạng tử**
    - Ví dụ: 3x, -5x²y, 7
    """)

    st.subheader("📌 Đa thức")
    st.write("""
    - Là tổng của **nhiều đơn thức**
    - Ví dụ: x² + 2x + 1
    """)

    st.info("👉 Mỗi hạng tử được ngăn cách bởi dấu + hoặc -")
    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NỘI DUNG 3: NHẬN DIỆN
# ===============================
elif menu == "🧠 Nhận diện đơn thức – đa thức":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    expr = st.text_input("✍️ Nhập một biểu thức đại số (ví dụ: x² + 3x):")

    if expr:
        if "+" in expr or "-" in expr.strip()[1:]:
            st.success("🔍 Đây là **ĐA THỨC**")
        else:
            st.success("🔍 Đây là **ĐƠN THỨC**")

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NỘI DUNG 4: LUYỆN TẬP
# ===============================
elif menu == "✍️ Luyện tập":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("📝 Bài tập")

    st.write("**Câu 1:** 5x² là đơn thức hay đa thức?")
    answer1 = st.radio("Chọn đáp án:", ["Đơn thức", "Đa thức"], key="q1")

    if st.button("Kiểm tra Câu 1"):
        if answer1 == "Đơn thức":
            st.success("✅ Chính xác!")
        else:
            st.error("❌ Chưa đúng. Hãy xem lại khái niệm.")

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NỘI DUNG 5: KIỂM TRA NHANH
# ===============================
elif menu == "📝 Kiểm tra nhanh":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("⏱️ Tự đánh giá nhanh")

    score = 0
    q = st.radio("x² + x có mấy hạng tử?", ["1", "2", "3"])

    if st.button("Nộp bài"):
        if q == "2":
            score = 10
        st.success(f"🎉 Điểm của em: {score}/10")

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# NỘI DUNG 6: TRỢ GIẢNG AI
# ===============================
elif menu == "🤖 Trợ giảng AI (Tự học ở nhà)":
    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader("🤖 Trợ giảng AI – Chủ đề Đơn thức, Đa thức")

    st.warning("""
    ⚠️ LƯU Ý QUAN TRỌNG  
    - AI chỉ **gợi ý – giải thích**, không giải thay  
    - Chỉ dùng khi **tự học ở nhà**  
    - Không dùng khi kiểm tra, thi  
    """)

    question = st.text_area(
        "✍️ Em hãy nhập câu hỏi về Đơn thức – Đa thức:",
        height=120
    )

    if st.button("📘 Nhận gợi ý từ trợ giảng AI"):
        if question.strip() != "":
            prompt = f"""
            Bạn là trợ giảng Toán lớp 8.
            Chủ đề: Đơn thức – Đa thức.
            Yêu cầu:
            - Giải thích ngắn gọn, dễ hiểu
            - Không giải toàn bộ bài
            - Chỉ gợi ý từng bước
            - Phù hợp chương trình Toán 8
            Câu hỏi của học sinh: {question}
            """
            response = model.generate_content(prompt)
            st.success("📗 Gợi ý học tập:")
            st.write(response.text)
        else:
            st.error("❗ Em cần nhập câu hỏi trước.")

    st.markdown("</div>", unsafe_allow_html=True)
