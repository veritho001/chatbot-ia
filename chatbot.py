
import streamlit as st

st.set_page_config(page_title="Carlos tu tutor virtual")
st.title("Carlos tu tutor virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def responder(texto):
    texto = texto.lower()

    if "hola" in texto:
        return "¡Hola! Soy Carlos, tu tutor virtual. ¿En qué puedo ayudarte?"
    elif "python" in texto:
        return "Python es un lenguaje de programación muy utilizado por su facilidad y versatilidad."
    elif "streamlit" in texto:
        return "Streamlit permite crear aplicaciones web con Python de forma rápida."
    elif "gracias" in texto:
        return "¡De nada! Me alegra haberte ayudado."
    else:
        return f"Entendí que escribiste: '{texto}'. Cuéntame más."

if prompt := st.chat_input("Escribe tu mensaje..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    respuesta = responder(prompt)

    st.session_state.messages.append({"role": "assistant", "content": respuesta})

    with st.chat_message("assistant"):
        st.markdown(respuesta)
