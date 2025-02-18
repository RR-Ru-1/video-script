import streamlit as st
from regex import search

from utils import generate_script

st.title("🎬 视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入API密钥:", type="password")

subject = st.text_input("💡 请输入视频的主题")

video_length = st.number_input("⌛️ 请输入视频时长（单位：分钟）", min_value = 0.1, step=0.1)

creativity = st.slider("💭 请输入本视频的创造力（数字越小越严谨，越大越多样）", min_value=0.1, max_value=1.0, value=0.5, step=0.1)

submit = st.button("生成脚本")

if submit and not openai_api_key:
    st.info("请输入API密钥")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit:
    with st.spinner("AI 正在思考，请稍等...."):
        title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已生成")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)
