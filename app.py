import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# st.header('娇娇和牛牛的AIGC World')
st.header('上海XXX人工智能科技有限公司')
# 显示图片
st.write("RAG process flow：")
# 加载图片
image = Image.open(r'S:\streamlit_study\figures\flow_chart.png')
width, height = 600, 400
image = image.resize((width, height))
# 在Streamlit中显示图片
st.image(image)
# 在Streamlit中显示图片并使其居中
#st.write(image)

st.subheader('First Demo，这是一个垂直领域工作助手前端展示！')
st.text('Description:本公司是一家新兴科技企业，致力于解决传统公司的数字化转型，提供各类数字化升级工作！')


# 创建一个文本输入框，并获取用户输入的name
user_input = st.text_input("Your name：")
# 显示用户输入的文本
st.write("Your name：", user_input)


# 定义模型选项
options = ['gpt-3.5-turbo', 'gpt-4', 'ChatGLM']
# 创建一个选择框，并获取用户选择的选项
choice = st.selectbox('1.选择你想用的模型：', options)
# 显示用户选择的选项
st.write('你选择的模型是：', choice)

# 定义垂直领域选项
options = ['法律', '金融', '教育', '医疗', '其他']

# 创建一个选择框，并获取用户选择的选项
choice = st.selectbox('2.选择您的行业：', options)

# 显示用户选择的选项
st.write('你选择的行业是：', choice)

st.write("开始你的AI之旅吧！")
# 创建一个文本输入框，并获取用户输入的文本
user_input = st.text_input("Q：")
# 显示答案
st.write("A:", user_input)




# st.markdown('这是 **Markdown** 文本。用来展示图表效果')
# st.latex(r'e^{i\pi} + 1 = 0')
# st.dataframe({'列1': [1, 2, 3], '列2': [4, 5, 6]})


#chart_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
#st.line_chart(chart_data)

#number = st.slider('请选择一个数字', 0, 100)
#st.write('您选择的数字是：', number)