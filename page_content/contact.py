import streamlit as st

def contact_page():
    # 注入按钮样式（全局 + 单独 Send Message 按钮）
    st.markdown("""
    <style>
    .custom-submit {
        background-color: #ffffff !important;
        color: #2c2c2c !important;
        border: 2px solid #a8977b !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        padding: 0.5rem 1.3rem !important;
        border-radius: 8px !important;
        transition: all 0.2s ease;
    }

    .custom-submit:hover {
        background-color: #f3ede1 !important;
        border-color: #8d7e61 !important;
        cursor: pointer;
    }

    .submit-wrapper {
        margin-top: 1rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Contact Me")

    st.markdown("""
    Feel free to reach out to me through any of the following channels:

    ### Direct Contact
    - **Email**: [klausyq@163.com](mailto:klausyq@163.com)
    - **Wechat**: Klaus_wyq
    - **Phone**: (+86) 176-0219-0677
    - **LinkedIn**: [linkedin.com/in/klaus-wang](https://linkedin.com/in/klaus-wang)
    - **GitHub**: [github.com/KlausYQ](https://github.com/KlausYQ)
    """)

    st.markdown("### Send Me a Message")

    with st.form("contact_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")

        with col2:
            subject = st.text_input("Subject")

        message = st.text_area("Message", height=150)

        # 这个 submit 按钮保持默认行为，但我们用 JS 在加载后替换样式
        submitted = st.form_submit_button("Send Message")

        # 处理提交逻辑
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")

    # 手动注入 JS 给 submit 按钮加 class（只需一次性精准匹配）
    st.markdown("""
    <script>
    setTimeout(() => {
        const btns = window.parent.document.querySelectorAll('button');
        for (let b of btns) {
            if (b.innerText.trim() === 'Send Message') {
                b.classList.add('custom-submit');
                break;
            }
        }
    }, 100);
    </script>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    ### Availability
    I'm currently based in Shenzhen and available for virtual meetings or phone call on weekdays (Monday to Friday), 10 AM to 8 PM. Feel free to email me in advance to schedule a chat.
    """)
