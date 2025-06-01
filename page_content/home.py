import base64
import streamlit as st
from PIL import Image
import os

def home_page():
    # 动画标题（桌面端用 CSS，移动端用 JS）
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@700&display=swap');

/* 桌面端：打字机动画 */
.typing-desktop {
    font-family: 'Rubik', sans-serif;
    font-size: 50px;
    font-weight: 800;
    color: #7B5131;
    white-space: nowrap;
    overflow: hidden;
    width: 0;
    animation: typing 3s steps(30, end) forwards;
    text-align: center;
    margin: 0 auto 1.5rem auto;
    max-width: 100%;
    display: block;
}

/* 桌面端动画帧 */
@keyframes typing {
    from { width: 0 }
    to { width: 100% }
}

/* 移动端：隐藏桌面动画，显示 JS 容器 */
@media screen and (max-width: 768px) {
    .typing-desktop {
        display: none;
    }
    #mobile-typing {
        display: block !important;
    }
}

/* 默认隐藏移动端动画容器（桌面不显示） */
#mobile-typing {
    display: none;
    text-align: center;
    font-family: 'Rubik', sans-serif;
    font-size: 32px;
    font-weight: 800;
    color: #7B5131;
    margin-bottom: 1.5rem;
    padding: 0 10px;
    word-wrap: break-word;
}
</style>

<!-- 桌面端标题 -->
<div class="typing-desktop">Welcome to Klaus's Homepage</div>

<!-- 移动端 JS 动画 -->
<div id="mobile-typing"></div>
<script>
const text = "Welcome to Klaus's Homepage";
let i = 0;
function typeWriter() {
    if (i < text.length) {
        document.getElementById("mobile-typing").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter, 60);
    }
}
if (window.innerWidth <= 768) {
    typeWriter();
}
</script>
""", unsafe_allow_html=True)

    # 页面左右布局
    left_col, right_col = st.columns([3, 4])

    # 左列：个人信息
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

    # 右列：头像居中显示
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

    # About Me 区块
    st.markdown(
        """
        ### About Me
        I am currently pursuing a Master of Science in Marketing at The Chinese University of Hong Kong, building upon a solid foundation in international economics and business acquired through my dual bachelor's degrees from Shanghai University and the University of Technology Sydney.

        My academic background has been enriched by hands-on internship experiences across investment banking, asset management, and consulting. From conducting financial due diligence for New Third Board listings at Hongta Securities, to drafting promotional and bidding materials for public REITs at Huatai Securities, I have developed strong analytical, communication, and project execution skills.

        I am particularly passionate about bridging finance and marketing with data-driven insights. Whether performing industry research, constructing client-facing documents, or supporting large-scale capital market transactions, I thrive in fast-paced, detail-oriented environments. I aim to contribute my diverse experience and international outlook to organizations at the intersection of strategy, investment, and market innovation.
        """
    )

    # Skills 区块
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
