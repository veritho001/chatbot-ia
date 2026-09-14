
import os
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(api_key=os.getenv("HF_TOKEN"))

st.set_page_config(page_title="Carlos tu tutor virtual")
st.title("Carlos tu tutor virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    respuesta = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Eres Carlos, un tutor virtual amable."}
        ] + st.session_state.messages,
        max_tokens=300
    )

    texto = respuesta.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": texto}
    )

    with st.chat_message("assistant"):
        st.markdown(texto)
