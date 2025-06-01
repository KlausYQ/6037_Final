import base64
import streamlit as st
from PIL import Image
import os

def home_page():
    # 页面动画与样式设置（移动端兼容）
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@700&display=swap');

/* 桌面端打字动画 */
.typing-container {
    font-family: 'Rubik', sans-serif;
    font-size: 50px;
    font-weight: 800;
    color: #7B5131;
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    animation: typing 3s steps(30, end) forwards;
    margin: 0 auto 1.5rem auto;
    text-align: center;
}

/* 动画关键帧 */
@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

/* 移动端样式：关闭动画，自动换行 */
@media screen and (max-width: 768px) {
    .typing-container {
        font-size: 28px;
        white-space: normal;
        animation: none;
        width: auto;
    }
}
</style>

<div class="typing-container">Welcome to Klaus's Homepage</div>
""", unsafe_allow_html=True)

    # 页面左右布局
    left_col, right_col = st.columns([3, 4])

    # 左列个人信息
    left_col.markdown(
        """
        <h2>Yuqi Wang (Klaus)</h2>
        <p>Master of Science in Marketing<br> 
        The Chinese University of Hong Kong, Business School<br>
        <br>
        Bachelor of Economics, International Economics & Trade<br>
        Shanghai University, SILC Business School<br>
        <br>
        Bachelor of Business, International Business<br>
        University of Technology Sydney, SILC Business School<br>
        <br>
        Email: <a href="mailto:klausyq@163.com">klausyq@163.com</a><br>
        Wechat: Klaus_wyq<br>
        Phone: (+86) 176-0219-0677</p>
        """,
        unsafe_allow_html=True
    )

    # 右列头像居中显示
    image_path = os.path.join("static", "images", "klaus.jpg")
    if os.path.exists(image_path):
        with right_col:
            with open(image_path, "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode()

            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; margin-top: 10px;">
                    <img src="data:image/png;base64,{img_base64}" 
                         width="350" style="border-radius: 10px;" />
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    # About Me 部分
    st.markdown(
        """
        ### About Me
        I am currently pursuing a Master of Science in Marketing at The Chinese University of Hong Kong, building upon a solid foundation in international economics and business acquired through my dual bachelor's degrees from Shanghai University and the University of Technology Sydney.

        My academic background has been enriched by hands-on internship experiences across investment banking, asset management, and consulting. From conducting financial due diligence for New Third Board listings at Hongta Securities, to drafting promotional and bidding materials for public REITs at Huatai Securities, I have developed strong analytical, communication, and project execution skills.

        I am particularly passionate about bridging finance and marketing with data-driven insights. Whether performing industry research, constructing client-facing documents, or supporting large-scale capital market transactions, I thrive in fast-paced, detail-oriented environments. I aim to contribute my diverse experience and international outlook to organizations at the intersection of strategy, investment, and market innovation.
        """
    )

    # Skills 部分
    st.markdown(
        """
        ### Skills
        - **Finance & Investment:** REITs, IPO due diligence, bond issuance support, financial modeling  
        - **Research & Analysis:** Policy interpretation, market trend analysis, report writing  
        - **Marketing & Strategy:** Business insight, stakeholder communication, promotional material creation  
        - **Tools:** Microsoft Office (Word, Excel, PowerPoint), Wind, iFind, Stata, Scopus, Scival, Python, R  
        - **Languages:** Mandarin (Native), English (Professional Working Proficiency, IELTS 7.0, GMAT 675)  
        - **Certifications:** CFA Level I, Securities & Banking Professional Qualification Certificate, Junior International Trade Specialist
        """
    )

    st.markdown("---")
