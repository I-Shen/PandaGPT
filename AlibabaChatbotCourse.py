# import streamlit as st
# import os
# import dashscope
# from dashscope import Generation

# # Set your key here
# DASHSCOPE_API_KEY = 'sk-73a711d8f68843de8632020b738d9545'
# dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'


# st.title("🐼 Ilmu Pengetahuan Panda")
# st.write("Panda Adalah Hewan Yang Suka Ingin Tahu, Coba Tanya Aku 🎋🐼")

# user_input = st.text_input("Isi Hati Pandaaa :")

# if st.button("Pencet Hidung 🐽"):
#     if not user_input.strip():
#         st.warning("Give me some food...")
#     else:
#         with st.spinner("Nyam Nyamm Nyammm..."):
#             try:
#                 messages = [
#                     {'role':'system','content':'you are a helpful assistant'},
#                     {'role': 'user','content': user_input}
#                 ]
#                 response = dashscope.Generation.call(
#                     # If environment variable is not configured, replace the line below with: api_key="sk-xxx",
#                     api_key=DASHSCOPE_API_KEY,
#                     model="qwen-plus", 
#                     messages=messages,
#                     result_format='message'
#                     )
#                 #response = Generation.call(model='qwen-plus', prompt=user_input)

#                 answer = response.output.choices[0].message.content
#                 st.markdown("### 🧠 Response:")
#                 st.success(answer)
#             except Exception as e:
#                 st.error(f"An error occurred: {str(e)}")

import streamlit as st
import dashscope
from dashscope import Generation

# API Key DashScope
DASHSCOPE_API_KEY = 'sk-73a711d8f68843de8632020b738d9545'
dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'

# Styling CSS
st.markdown(
    """
    <style>
        body {
            background-color: #E6F0D5;
        }
        .panda-logo {
            font-size: 130px;
            text-align: center;
            margin-bottom: -5px;
            margin-top: 10px;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-top: 0px;
            margin-bottom: 10px;
        }
        .main-subtitle {
            text-align: center;
            font-size: 20px;
            margin-top: 0px;
            margin-bottom: 10px;
        }
        .stTextInput>div>div>input {
            text-align: center;
        }
        .block-container {
            padding-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 🐼 Ikon Panda Besar
st.markdown('<div class="panda-logo">🐼</div>', unsafe_allow_html=True)

# Judul Tengah
st.markdown('<div class="main-title">Ilmu Pengetahuan Panda</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">PandaGPT Adalah Hewan Yang Suka Ingin Tahu, Coba Tanya Aku 🎋🐼</div>', unsafe_allow_html=True)

# Input Pengguna
user_input = st.text_input("Isi Hati Pandaaa :")

if st.button("Pencet idung 🐽"):
    if not user_input.strip():
        st.warning("Give me some food...")
    else:
        with st.spinner("Nyam Nyamm Nyammm..."):
            try:
                messages = [
                    {'role': 'system', 'content': 'you are a helpful assistant'},
                    {'role': 'user', 'content': user_input}
                ]
                response = dashscope.Generation.call(
                    api_key=DASHSCOPE_API_KEY,
                    model="qwen-plus",
                    messages=messages,
                    result_format='message'
                )
                answer = response.output.choices[0].message.content
                st.markdown("### 🧠 Response:")
                st.success(answer)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

