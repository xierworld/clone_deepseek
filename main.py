import streamlit as st
from streamlit import chat_input, spinner

from utils import get_chat_response
from langchain.memory import ConversationBufferMemory

st.title("克隆deepseek")
with st.sidebar:
    deepseek_api_key = st.text_input("请输入你的deepseek_api密钥：", type="password")
    st.markdown("[获取deepseek api密钥](https://platform.deepseek.com/api_keys)")

if "memory" not in st.session_state or "message" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["message"] = [{"role": "ai", "content": "你好，我是你的AI助手，有什么可以帮你的？"}]

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = chat_input()
if prompt:
    if not deepseek_api_key:
        st.info("请输入deepseek_api密钥")
        st.stop()
    st.session_state["message"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with spinner("AI正在思考中，请稍等..."):
        respense = get_chat_response(prompt, st.session_state["memory"], deepseek_api_key)
    msg = {"role": "ai", "content": respense}
    st.session_state["message"].append(msg)
    st.chat_message("ai").write(respense)