import streamlit as st


def experience_page():
    st.markdown("## Internship Experience")

    st.markdown("""
    ### Investment Banking Intern  
    **Hongta Securities, Investment Banking Division** | *Jul 2023 – Sep 2023*  
    - Assisted with due diligence and documentation for a major equity financing project, contributing to the preparation of internal and external roadshows.  
    - Participated in feasibility studies and financial analysis for M&A and REITs projects, enhancing understanding of capital markets and structured financing.  
    - Developed pitch books and industry reports by collecting and analyzing public market data.
    """)

    st.markdown("""
    ### Real Estate Finance Intern  
    **Huatai Securities, REITs Department** | *Jan 2023 – Mar 2023*  
    - Supported senior analysts in preparing valuation models and investment summaries for real estate trust products.  
    - Engaged in the drafting of REITs issuance reports and assisted in regulatory filings and disclosures.  
    - Gained experience with REITs structure and regulatory environment in China.
    """)

    st.markdown("""
    ### Business Analyst Intern  
    **IDM Consulting** | *Jun 2022 – Aug 2022*  
    - Conducted industry and market analysis for clients in the fast-moving consumer goods sector.  
    - Built PowerPoint decks and Excel-based financial models to support strategic recommendations.  
    - Participated in client meetings and helped summarize minutes and key action points.
    """)

    st.markdown("""
    ### Investment Intern  
    **Yunnan Tin Investment Co., Ltd.** | *Jan 2022 – Feb 2022*  
    - Collected and evaluated financial and operational data for mining industry investments.  
    - Assisted in risk assessments for potential projects and prepared internal investment memos.  
    - Supported ongoing post-investment tracking and report writing.
    """)

    st.markdown("---")

    st.markdown("## Projects")

    projects = [
        {
            "title": "Customer Segmentation and Conversion Analysis for JD.com",
            "description": "Conducted in-depth analysis of JD.com’s high-value and non-high-value customers using e-commerce data to identify behavioral patterns and improve targeting strategies.",
            "skills": ["R", "Data Cleaning", "Segmentation", "Conversion Funnel Analysis", "Visualization"],
            "outcome": "Identified distinct shopping behaviors across customer tiers; provided actionable insights to increase conversion efficiency and optimize marketing strategies.",
            "file_path": "static/docs/Project-JD.pdf",
            "file_name": "Project-JD.pdf"
        },
        {
            "title": "Digital Strategy and Brand Positioning for 999 Sanjiu Piyanping",
            "description": "Collaborated with CR Sanjiu to analyze brand pain points including product homogeneity, market confusion, and reputation risk due to food safety issues, using multi-platform data.",
            "skills": ["Python", "Social Media Analysis", "Sentiment Analysis", "KOL Mapping", "Strategy Recommendation"],
            "outcome": "Proposed a three-tiered solution involving product restructuring, youth branding, and targeted communication strategy based on real user feedback and digital traces.",
            "file_path": "static/docs/Project-Sanjiu.pdf",
            "file_name": "Project-Sanjiu.pdf"
        },
        {
            "title": "Consumer Insight and Brand Influence Analysis for Jellycat",
            "description": "Performed multi-platform data mining (Instagram, Xiaohongshu, Bilibili) to assess user reinterpretation of Jellycat toys and its impact on brand resonance and visual engagement.",
            "skills": ["Python", "UGC Analysis", "Image & Color Analysis", "Text Mining", "Topic Modeling"],
            "outcome": "Uncovered key visual trends and emotional anchors that enhance user interaction and provided branding strategies to amplify Jellycat’s appeal among Gen Z consumers.",
            "file_path": "static/docs/Project-Jellycat.pdf",
            "file_name": "Project-Jellycat.pdf"
        }
    ]

    for i, project in enumerate(projects):
        with st.expander(f"Project {i+1}", expanded=i == 0):
            st.markdown(
                f"<div style='font-size:20px; font-weight:bold; margin-bottom:8px'>{project['title']}</div>",
                unsafe_allow_html=True
            )
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")

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



    st.markdown("---")

    st.markdown("## Professional Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, Stata
        - **Marketing Analytics:** A/B Testing, Sentiment Analysis, Segmentation
        - **Data Processing:** Pandas, NumPy, tidyverse
        - **Visualization:** ggplot2, Tableau, PowerBI
        - **Statistical Modeling:** Regression, Hypothesis Testing, ANOVA
        - **Tools:** Excel (VBA), SPSS, LaTeX
        """)

    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Bilingual Presentation and Business Writing (Chinese/English)
        - **Teamwork:** Experienced in cross-functional, multicultural collaboration
        - **Problem-solving:** Data-driven decision making with strong business acumen
        - **Time Management:** Multi-project coordination with efficient time allocation
        - **Leadership:** Led academic teams and mentored junior students in competitions
        - **Adaptability:** Agile in fast-paced environments and new tools
        """)

    st.markdown("---")
