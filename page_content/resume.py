import streamlit as st
import base64
import os

def resume_page():
    st.title("LEI LEI")

    # 所有现有的内容保持不变
    st.header("Contact Information")
    st.markdown("""
    - **Email:** lleirosalie@163.com
    - **Phone:** (+852) 4662 8851
    - **LinkedIn:** [linkedin.com/in/janedoe](https://www.linkedin.com/in/lei-lei-7b0200346/)
    - **GitHub:** [github.com/janedoe](https://github.com/rosalielei)
    - **Address:** 8 Shan Tong Road, Mid-Levels, Tai Po, New Territories, Hong Kong
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly analytical Master's candidate in Marketing (CUHK) with a strong foundation in Economics (ECNU) and international experience (UC Berkeley). Proven ability to drive marketing growth and optimize performance using data analytics, market research, and digital strategies. Seeking a challenging marketing or data-driven role to apply advanced analytical and cross-cultural communication skills.
    """)

    st.markdown("---")

    # 添加PDF预览部分
    st.header("Resume Download")
    
    pdf_path = "static/docs/resume.pdf"
    if os.path.exists(pdf_path):
        # 首先读取PDF文件
        with open(pdf_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        # 添加下载按钮
        st.download_button(
            label=" 📄 Resume Download",
            data=PDFbyte,
            file_name="resume_LEI_LEI.pdf",
            mime="application/pdf"
        )
        
        # 添加PDF图片预览
        st.header("Resume Preview")
        st.image("static/docs/resume.pdf", caption="Resume Preview", use_column_width=True)
    else:
        st.error("The PDF file was not found. Please ensure that 'resume.pdf' exists in the static/docs directory.")