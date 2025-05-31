import streamlit as st
from rizz_model import generate_rizz

st.set_page_config(page_title="RizzBot", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #0f111b;
        color: #d1d5db;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #1f2937;
        color: #d1d5db;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 18px;
    }
    .stButton>button {
        background-color: #22c55e;
        color: #0f111b;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #16a34a;
    }
    .response-box {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 18px;
        color: #d1d5db;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💬 RizzBot - Your AI Wingman")

user_input = st.text_input("Send a message:", placeholder="Type a message here...")

if user_input:
    with st.spinner("Generating rizz..."):
        response = generate_rizz(user_input)
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)
