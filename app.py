import streamlit as st

st.set_page_config(page_title="Football AI", page_icon="⚽", layout="wide")

st.title("⚽ 足球人工智能专业云平台")
st.success("✅ 系统启动成功！")

tab1, tab2 = st.tabs(["LiveData", "AIPrediction"])

with tab1:
    st.header("实时数据看板")
    st.write("多源抓取模块已就绪。")

with tab2:
    st.header("AI 预测模型")
    st.write("正在连接历史数据库与三赛季表现分析...")

