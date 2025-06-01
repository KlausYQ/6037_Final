import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(label="📄 Download Resume (PDF)",
                        data=PDFbyte,
                        file_name="Yuqi_Wang_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Yuqi Wang")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** [klausyq@163.com](mailto:klausyq@163.com)
    - **Wechat**: Klaus_wyq
    - **Phone:** (+86) 176-0219-0677
    - **LinkedIn:** [linkedin.com/in/klaus-wang](https://linkedin.com/in/klaus-wang)
    - **GitHub:** [github.com/klaus-wang](https://github.com/klaus-wang)
    """)

    st.header("Professional Summary")
    st.markdown("""
    Graduate student in Marketing at The Chinese University of Hong Kong with dual bachelor's degrees in Economics and Business.  
    Experienced across investment banking, asset management, and consulting, with a strong foundation in REITs, market research, and business strategy.  
    Passionate about integrating finance, policy, and marketing insights into impactful decision-making.
    """)

    st.header("Education")
    st.markdown("""
    **MSc in Marketing**  
    - The Chinese University of Hong Kong  
    - *Aug 2024 – Present*

    **Bachelor of Economics, International Economics & Trade**  
    - Shanghai University, SILC Business School  
    - *Sep 2018 – Jul 2022*  
    - GPA: 3.25/4.0

    **Bachelor of Business, International Business**  
    - University of Technology Sydney (Joint Program)  
    - *Aug 2020 – May 2022*  
    - GPA: 5.38/7.0
    """)

    st.header("Internship Experience")
    st.markdown("""
    **Investment Banking Intern**  
    *Hongta Securities Co., Ltd.* | *Mar 2024 – Jun 2024*  
    - Participated in on-site financial due diligence for New Third Board listing, validating two years of corporate financial data  
    - Drafted a 50-page advisory report for a scenic area SOE, covering industry outlook and strategic recommendations  
    - Supported internal knowledge base with over 20 internal case summaries on IPOs and bond reviews  

    **REITs Project Intern**  
    *Huatai Securities (Shanghai) Asset Management Co., Ltd.* | *Mar 2023 – Jun 2023*  
    - Drafted over 10 sets of REITs promotional materials (50–90 pages) and four 200+ page bidding proposals for SOE infrastructure deals  
    - Composed policy response letters and screened underlying assets using financial and compliance metrics  

    **Research Analyst Intern**  
    *IDM Research Co., Ltd.* | *Feb 2022 – Jun 2022*  
    - Assisted in university evaluation for C9/E9/"Double First-Class" institutions  
    - Maintained a scholar database for consulting use, and co-authored reports on Huawei-Ericsson global collaborations  

    **Business Intern**  
    *Yunnan Tin (Shanghai) Investment Development Co., Ltd.* | *May 2021 – Aug 2021*  
    - Managed contract workflows, invoicing, client communication, and documentation  
    - Coordinated with internal teams to resolve over 30 client issues with >95% satisfaction
    """)

    st.header("Skills")
    st.markdown("""
    - **Quantitative Analysis:** Econometrics, Policy Modeling, Financial Forecasting  
    - **Tools:** Wind, iFind, Office Suite, Stata, Scival, Scopus, Python, R  
    - **Marketing & Strategy:** 4P Model, Market Planning, Consumer Insights, Report Writing  
    - **Languages:** English (IELTS 7.0, GMAT 675), Mandarin (Native)  
    - **Soft Skills:** Attention to Detail, Cross-Team Collaboration, Research Communication
    """)

    st.header("Certifications")
    st.markdown("""
    - CFA Level I *(Passed)*  
    - Securities Qualification Certificate  
    - Junior International Trade Specialist  
    - Banking Professional Qualification Certificate
    """)

    st.header("Projects")
    st.markdown("""
    **International Volunteer Program (U.S.)**  
    *Therapeutic Equestrian Services Project*  
    - Provided guided assistance and support to clients with physical and psychological disabilities during equine therapy sessions  
    - Completed professional training and served over 30 clients with an A+ service satisfaction rating  
    - Led weekly team meetings and documented 12 full service reports  

    **Trainee Barista Program – Harvest Coffee, Dali**  
    - Trained in specialty coffee preparation, customer service, and promotional sales  
    - Designed and launched over 20 marketing visuals and pushed sales to grow 24% month-over-month  
    - Managed inventory and coordinated with suppliers, supporting event-based customer outreach
    """)

    st.header("Languages")
    st.markdown("""
    - **Mandarin:** Native  
    - **English:** Professional Working Proficiency
    """)

    st.header("Interests")
    st.markdown("""
    - Football (University Champion)  
    - Basketball (University Runner-up)  
    - Singing (Top 10 Singer at Shanghai University)  
    - Badminton, Fitness & Strength Training  
    - Specialty Coffee Brewing & Tasting  
    - Wine Appreciation & Mixology  
""")


    st.markdown("---")
