import streamlit as st
st.header('AIGC World')
st.subheader('First')
st.text('Description')
st.markdown('这是 **Markdown** 文本。')
st.latex(r'e^{i\pi} + 1 = 0')
st.dataframe({'列1': [1, 2, 3], '列2': [4, 5, 6]})

import numpy as np
import pandas as pd
chart_data = pd.DataFrame(np.random.randn(50, 3), columns=['a', 'b', 'c'])
st.line_chart(chart_data)

number = st.slider('选择一个数字', 0, 100)
st.write('您选择的数字是：', number)