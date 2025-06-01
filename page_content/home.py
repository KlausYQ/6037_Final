import streamlit as st
from PIL import Image
import os

def home_page():
    # 打字机动画标题（无闪烁光标 + 更好看的字体）
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@700&display=swap');

.typing-container {
    font-family: 'Rubik', sans-serif;
    font-size: 50px;
    font-weight: 800;
    color:#7B5131;
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    animation: typing 3s steps(500, end) forwards;
    margin-bottom: 1.5rem;
}
@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

/* 居中右侧图片 */
.center-image {
    display: flex;
    justify-content: center;
    margin-top: 10px;
}
</style>

<div class="typing-container">Welcome to Klaus's Homepage</div>
""", unsafe_allow_html=True)

    left_col, right_col = st.columns([3, 4])

    # 左列内容
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

    # 右列居中显示照片
    image_path = os.path.join("static", "images", "klaus.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        width, height = image.size
        new_width = 300
        new_height = int(height * (new_width / width))
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        with right_col:
            st.markdown('<div class="center-image">', unsafe_allow_html=True)
            st.image(image, output_format="PNG", use_column_width=False)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    # About Me
    st.markdown(
        """
        ### About Me
        I am currently pursuing a Master of Science in Marketing at The Chinese University of Hong Kong, building upon a solid foundation in international economics and business acquired through my dual bachelor's degrees from Shanghai University and the University of Technology Sydney.

        My academic background has been enriched by hands-on internship experiences across investment banking, asset management, and consulting. From conducting financial due diligence for New Third Board listings at Hongta Securities, to drafting promotional and bidding materials for public REITs at Huatai Securities, I have developed strong analytical, communication, and project execution skills.

        I am particularly passionate about bridging finance and marketing with data-driven insights. Whether performing industry research, constructing client-facing documents, or supporting large-scale capital market transactions, I thrive in fast-paced, detail-oriented environments. I aim to contribute my diverse experience and international outlook to organizations at the intersection of strategy, investment, and market innovation.
        """
    )

    # Skills
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
