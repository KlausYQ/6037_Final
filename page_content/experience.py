import streamlit as st
import os

def experience_page():
    # 样式设置：页签 + 项目标题 + 技能页签加粗
    st.markdown("""
    <style>
    /* Tabs 样式 */
    div[data-testid="stTabs"] button {
        font-size: 20px !important;
        font-weight: 700 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease;
        border-radius: 8px !important;
    }

    div[data-testid="stTabs"] button:hover {
        background-color: #f2f2f2 !important;
        transform: scale(1.03);
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #e4dcc5 !important;
        border-bottom: 3px solid #a8977b !important;
    }

    /* Skills 区块标题字体统一放大 */
    .skills-title {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #2c2c2c;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Experience & Projects")

    tabs = st.tabs(["Internships", "Projects", "Skills"])

    # ========== Internship Tab ==========
    with tabs[0]:
        st.markdown("""
        ### Investment Banking Intern  
        **Hongta Securities, Investment Banking Division** | *Jul 2023 – Sep 2023*  
        - Assisted with due diligence and documentation for a major equity financing project.  
        - Participated in feasibility studies and financial analysis for M&A and REITs projects.  
        - Developed pitch books and industry reports.

        ### Real Estate Finance Intern  
        **Huatai Securities, REITs Department** | *Jan 2023 – Mar 2023*  
        - Prepared valuation models and investment summaries for real estate trust products.  
        - Assisted in REITs issuance reports and regulatory filings.

        ### Business Analyst Intern  
        **IDM Consulting** | *Jun 2022 – Aug 2022*  
        - Conducted industry and market analysis for FMCG clients.  
        - Built financial models and presentation materials.  
        - Attended client meetings and summarized key actions.

        ### Investment Intern  
        **Yunnan Tin Investment Co., Ltd.** | *Jan 2022 – Feb 2022*  
        - Evaluated financial data for mining sector investments.  
        - Contributed to internal investment memos and post-investment reports.
        """)

    # ========== Projects Tab ==========
    with tabs[1]:
        projects = [
            {
                "title": "Customer Segmentation and Conversion Analysis for JD.com",
                "description": "Analyzed JD.com’s high-value vs non-high-value customer behaviors to optimize marketing.",
                "skills": ["R", "Data Cleaning", "Segmentation", "Funnel Analysis", "Visualization"],
                "outcome": "Revealed behavioral differences to inform targeting strategies.",
                "file_path": "static/docs/Project-JD.pdf",
                "file_name": "Project-JD.pdf"
            },
            {
                "title": "Digital Strategy for 999 Piyanping",
                "description": "Identified brand weaknesses and crafted youth-oriented branding strategy via social data.",
                "skills": ["Python", "Sentiment Analysis", "KOL Mapping"],
                "outcome": "Proposed product restructuring and targeted digital communication.",
                "file_path": "static/docs/Project-Sanjiu.pdf",
                "file_name": "Project-Sanjiu.pdf"
            },
            {
                "title": "Brand Influence Analysis for Jellycat",
                "description": "Used UGC and visual mining to reveal Jellycat’s emotional and visual resonance trends.",
                "skills": ["Python", "UGC Analysis", "Topic Modeling"],
                "outcome": "Provided branding suggestions for Gen Z engagement.",
                "file_path": "static/docs/Project-Jellycat.pdf",
                "file_name": "Project-Jellycat.pdf"
            }
        ]

        for i, project in enumerate(projects):
            with st.expander(f"Project {i+1}", expanded=i == 0):
                st.markdown(f"""
                <div style='font-size: 20px; font-weight: 700; margin-bottom: 0.5rem;'>
                    {project['title']}
                </div>
                <div><strong>Description:</strong> {project['description']}</div>
                <div><strong>Skills Used:</strong> {', '.join(project['skills'])}</div>
                <div><strong>Outcome:</strong> {project['outcome']}</div>
                """, unsafe_allow_html=True)

                try:
                    with open(project["file_path"], "rb") as file:
                        st.download_button(
                            label="📄 Download Project Report",
                            data=file,
                            file_name=project["file_name"],
                            mime="application/pdf"
                        )
                except FileNotFoundError:
                    st.warning("Project file not found.")

    # ========== Skills Tab ==========
    with tabs[2]:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("<div class='skills-title'>Technical Skills</div>", unsafe_allow_html=True)
            st.markdown("""
            - **Languages & Tools:** Python, R, SQL, Stata, Excel (VBA), SPSS  
            - **Data Science:** Regression, ANOVA, A/B Testing, Clustering  
            - **Marketing Analytics:** Sentiment Analysis, Topic Modeling, UGC Mining  
            - **Visualization:** Tableau, Power BI, ggplot2, matplotlib
            """)

        with col2:
            st.markdown("<div class='skills-title'>Soft Skills</div>", unsafe_allow_html=True)
            st.markdown("""
            - **Communication:** Bilingual (Chinese/English)  
            - **Teamwork:** Cross-functional, multicultural collaboration  
            - **Problem-solving:** Data-driven business solutions  
            - **Time Management:** Efficient multi-project handling  
            - **Leadership:** Led academic teams, mentored peers  
            - **Adaptability:** Fast learner in new tools and settings
            """)
