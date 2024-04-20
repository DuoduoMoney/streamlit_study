import streamlit as st

# 在应用程序中添加文本
st.title("我的第一个 Streamlit 应用程序")
st.write("欢迎使用 Streamlit！这是一个简单的示例。")

# 添加交互元素
user_input = st.text_input("请输入您的姓名：")
st.write("你好，", user_input, "!")

# 绘制图表
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
plt.hist(data, bins=20)
st.pyplot(plt)

# 显示数据框
import pandas as pd

df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 22]
})

st.write("这是一个简单的数据框：")
st.dataframe(df)

# 添加图表和地图
st.line_chart(np.random.randn(20, 2) + 10)
st.map({'杭州': (30.2500, 120.1500), '北京': (39.9042, 116.4074)})

# 添加侧边栏
st.sidebar.header("侧边栏")
st.sidebar.checkbox("显示/隐藏数据框", True)
selected_data = st.sidebar.selectbox("选择数据", df['姓名'])
st.sidebar.write(f"你选择了 {selected_data}")

# 添加按钮
if st.button("点击我"):
    st.write("你点击了按钮！")

# 添加进度条
import time

with st.spinner("加载中..."):
    time.sleep(3)
    st.success("加载完成!")

# 添加警告和错误
st.warning("这是一个警告信息")
st.error("这是一个错误信息")
