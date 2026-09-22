
import streamlit as st

st.set_page_config(
    page_title="Carlos Tutor Virtual 2.0",
    page_icon="🤖",
    layout="centered"
)

# ---------- Barra lateral ----------
st.sidebar.title("🤖 ChatBot 2.0")
st.sidebar.write("Carlos - Tutor Virtual")

st.sidebar.markdown("### Temas disponibles")
st.sidebar.markdown("""
- Python
- Streamlit
- Inteligencia Artificial
- Programación
- Base de Datos
- Redes
- Algoritmos
- Git y GitHub
""")

if st.sidebar.button("🗑️ Limpiar conversación"):
    st.session_state.messages = []
    st.rerun()

# ---------- Pantalla principal ----------
st.title("🤖 Carlos Tutor Virtual 2.0")
st.caption("Asistente para responder preguntas básicas de informática y programación.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def responder(texto):
    t = texto.lower()

    respuestas = {
        "hola": "¡Hola! Soy Carlos, tu tutor virtual. ¿En qué puedo ayudarte?",
        "python": "Python es un lenguaje de programación utilizado para desarrollar aplicaciones, automatizar tareas y analizar datos.",
        "streamlit": "Streamlit permite crear aplicaciones web interactivas usando Python.",
        "inteligencia artificial": "La inteligencia artificial permite que las computadoras realicen tareas similares al razonamiento humano.",
        "programación": "La programación consiste en crear instrucciones para resolver problemas mediante una computadora.",
        "base de datos": "Una base de datos almacena y organiza información para facilitar su consulta.",
        "redes": "Las redes permiten la comunicación entre dispositivos para compartir información y recursos.",
        "algoritmo": "Un algoritmo es una secuencia ordenada de pasos para resolver un problema.",
        "git": "Git es un sistema de control de versiones.",
        "github": "GitHub es una plataforma para almacenar repositorios y colaborar en proyectos."
    }

    for palabra, respuesta in respuestas.items():
        if palabra in t:
            return respuesta

    if "gracias" in t:
        return "¡Con gusto! Estoy aquí para ayudarte."

    if "adiós" in t or "bye" in t:
        return "¡Hasta luego! Que tengas un excelente día."

    return (
        "Aún soy una versión básica del ChatBot 2.0. "
        "Puedo responder preguntas sobre Python, Streamlit, programación, "
        "redes, algoritmos, Git, GitHub e inteligencia artificial."
    )

if prompt := st.chat_input("Escribe tu pregunta..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    respuesta = responder(prompt)

    st.session_state.messages.append({"role": "assistant", "content": respuesta})

    with st.chat_message("assistant"):
        st.markdown(respuesta)
