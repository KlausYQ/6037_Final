import streamlit as st
import os

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing  
    **The Chinese University of Hong Kong, Business School** | *August 2024 - November 2025*
    
    - Currently enrolled in the MSc in Marketing program
    - Relevant Coursework: Big Data Strategy (A), Digital Marketing (A-), Business Negotiation (A-), Marketing Management (A-)


    ### Bachelor of Economics, International Economics & Trade  
    **Shanghai University, SILC Business School** | *September 2018 – July 2022*
    
    - GPA: 3.25/4.0
    - Relevant Coursework: Econometrics (98), International Trade Lab (98), Monetary Banking (97), Management Accounting (97)

    ### Bachelor of Business, International Business  
    **University of Technology Sydney, SILC Business School** | *August 2020 – May 2022*
    
    - GPA: 5.38/7.0
    - Relevant Coursework: International Financial Management (3.7), Global Operations & Supply Chain Management (3.7), Global Business Environment (3.7)
    """)

    st.markdown("---")
    
    st.markdown("## Certifications")

    cert1, cert2, cert3, cert4 = st.columns(4)

    with cert1:
        st.markdown("""
        ### CFA Level I  
        **CFA Institute** | *Passed in June 2024*
        
        Demonstrated knowledge in investment tools, asset valuation, portfolio management, and ethical standards.
        """)
        if os.path.exists("static/docs/cfa_certificate.pdf"):
            with open("static/docs/cfa_certificate.pdf", "rb") as pdf_file:
                st.download_button(
                    label="Download Certification",
                    data=pdf_file,
                    file_name="cfa_certificate.pdf",
                    mime="application/pdf"
                )

    with cert2:
        st.markdown("""
        ### Junior International Trade Specialist  
        **CCPIT & CCOIC** | *Issued in January 2021*
        
        Credential demonstrating foundational knowledge in international trade practices and policies.
        """)
        if os.path.exists("static/docs/trade_specialist_cert.pdf"):
            with open("static/docs/trade_specialist_cert.pdf", "rb") as pdf_file:
                st.download_button(
                    label="Download Certification",
                    data=pdf_file,
                    file_name="trade_specialist_cert.pdf",
                    mime="application/pdf"
                )

    with cert3:
        st.markdown("""
        ### Securities Qualification Certificate  
        **Securities Association of China** | *Issued in June 2023*
        
        Certified understanding of securities regulations and market operations in China.
        """)
        if os.path.exists("static/docs/securities_cert.pdf"):
            with open("static/docs/securities_cert.pdf", "rb") as pdf_file:
                st.download_button(
                    label="Download Certification",
                    data=pdf_file,
                    file_name="securities_cert.pdf",
                    mime="application/pdf"
                )

    with cert4:
        st.markdown("""
        ### Banking Professional Qualification Certificate  
        **China Banking Association** | *Issued in June 2024*
        
        Validates core competencies and regulatory understanding required for banking professionals in China.
        """)
        if os.path.exists("static/docs/banking_cert.pdf"):
            with open("static/docs/banking_cert.pdf", "rb") as pdf_file:
                st.download_button(
                    label="Download Certification",
                    data=pdf_file,
                    file_name="banking_cert.pdf",
                    mime="application/pdf"
                )

    st.markdown("---")
    
    st.markdown("## Academic Projects")

    st.markdown("""
    ### Graduation Thesis: Impact of Stock Market Liberalisation on Cash Dividend Policy  
    **Shanghai-Hong Kong & Shenzhen-Hong Kong Stock Connect** | *Dec 2021 – May 2022*  
    - Collected panel data from A-share listed companies (2007–2019) and proposed four empirical hypotheses  
    - Constructed a difference-in-differences (DID) model to evaluate the impact of stock connect policies on corporate cash dividend levels  
    - Conducted robustness tests and explored policy mechanisms, heterogeneity across firm types, and spillover effects

    ### The 8th International Trade & Business Competition for Global College Students  
    **Empirical Study on Scale, Innovation Capability, and R&D Investment** | *Mar 2020 – Oct 2020*  
    - Analyzed data from U.S. industrial listed firms to examine how company scale and innovation capability affect uncertainty and R&D investment decisions  
    - Built regression models to test key hypotheses, identifying significant relationships between innovation inputs and market risk  
    - Delivered strategic insights for firms pursuing scalable innovation under uncertainty

    ### Individual Project: International Marketing Plan for Perfect World Games  
    **Course: International Marketing** | *Apr 2021 – Jun 2021*  
    - Assessed Perfect World's international brand positioning, market readiness, and revenue model in China and the U.S.  
    - Compared mobile gaming market environments and consumer behaviors across both regions  
    - Applied the 4P framework to design a market entry plan and conducted financial estimation to support go-to-market strategy
    """)
    
    st.markdown("---")
