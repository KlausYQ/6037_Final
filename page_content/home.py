import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns([1, 1.5])  # 给右列更多空间显示图片
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
    Phone: (+86) 176-0219-0677</p>
    """,
    unsafe_allow_html=True
)



# <p> is for paragraph,<br> is for break, change line

    # add a photo to the right column
    image_path = os.path.join("static", "images", "klaus.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        # 保持宽高比的情况下调整尺寸
        width, height = image.size
        new_width = 300
        new_height = int(height * (new_width / width))
        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        right_col.image(image, output_format="PNG")
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
    """
    ### About Me
    I am currently pursuing a Master of Science in Marketing at The Chinese University of Hong Kong, building upon a solid foundation in international economics and business acquired through my dual bachelor's degrees from Shanghai University and the University of Technology Sydney.

    My academic background has been enriched by hands-on internship experiences across investment banking, asset management, and consulting. From conducting financial due diligence for New Third Board listings at Hongta Securities, to drafting promotional and bidding materials for public REITs at Huatai Securities, I have developed strong analytical, communication, and project execution skills.

    I am particularly passionate about bridging finance and marketing with data-driven insights. Whether performing industry research, constructing client-facing documents, or supporting large-scale capital market transactions, I thrive in fast-paced, detail-oriented environments. I aim to contribute my diverse experience and international outlook to organizations at the intersection of strategy, investment, and market innovation.
    """
)


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
    
    # Interactive component has been moved to the experience page
