import streamlit as st
import numpy as np
import pandas as pd

st.header('娇娇和牛牛的AIGC World')
st.subheader('First Demo')
st.subheader('这是一个快速前端展示！')
st.subheader('哈哈哈')
st.text('Description')
st.markdown('这是 **Markdown** 文本。用来展示图表效果')
st.latex(r'e^{i\pi} + 1 = 0')
st.dataframe({'列1': [1, 2, 3], '列2': [4, 5, 6]})


chart_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

number = st.slider('请选择一个数字', 0, 100)
st.write('您选择的数字是：', number)