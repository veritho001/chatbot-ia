import streamlit as st
import time
from datetime import datetime

# ---------- Configuración ----------
st.set_page_config(
    page_title="Carlos Tutor Virtual 2.0",
    page_icon="🤖",
    layout="centered"
)

# ---------- Estilos ----------
st.markdown("""
<style>
.main{
    padding-top:1rem;
}
.block-container{
    max-width:900px;
}
h1{
    text-align:center;
}
.stChatMessage{
    border-radius:15px;
}
.stSidebar{
    background:#f8f9fa;
}
.tema{
    background:#eef3ff;
    padding:8px;
    border-radius:8px;
    margin-bottom:6px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Estado ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "contador" not in st.session_state:
    st.session_state.contador = 0

# ---------- Barra lateral ----------
with st.sidebar:

    st.title("🤖 Carlos 2.0")
    st.caption("Tutor Virtual")

    st.markdown("### Estado")
    st.write(f"💬 Mensajes: {st.session_state.contador}")

    st.markdown("---")

    st.markdown("### Temas disponibles")

    temas = [
        "Python",
        "Streamlit",
        "HTML",
        "CSS",
        "Java",
        "SQL",
        "Git",
        "GitHub",
        "Redes",
        "Ciberseguridad",
        "Base de Datos",
        "Algoritmos",
        "Inteligencia Artificial"
    ]

    for t in temas:
        st.markdown(f"<div class='tema'>📘 {t}</div>", unsafe_allow_html=True)

    st.markdown("---")

    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        st.session_state.messages = []
        st.session_state.contador = 0
        st.rerun()

# ---------- Encabezado ----------
st.title("🤖 Carlos Tutor Virtual 2.0")
st.caption("Asistente de informática y programación")

st.info("Puedes hacer preguntas sobre programación, redes, bases de datos y tecnología.")

# ---------- Preguntas rápidas ----------
st.markdown("### Preguntas rápidas")

col1, col2, col3 = st.columns(3)

pregunta = None

with col1:
    if st.button("¿Qué es Python?"):
        pregunta = "¿Qué es Python?"

with col2:
    if st.button("¿Qué es Git?"):
        pregunta = "¿Qué es Git?"

with col3:
    if st.button("¿Qué es IA?"):
        pregunta = "¿Qué es inteligencia artificial?"

# ---------- Mostrar historial ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "hora" in msg:
            st.caption(msg["hora"])

# ---------- Base de conocimiento ----------
def responder(texto):

    t = texto.lower()

    respuestas = {

        "hola":"¡Hola! Soy Carlos, tu tutor virtual. ¿En qué puedo ayudarte?",

        "python":"Python es un lenguaje de programación muy utilizado para desarrollar aplicaciones, automatizar tareas, crear inteligencia artificial y analizar datos.",

        "streamlit":"Streamlit es un framework de Python que permite crear aplicaciones web interactivas sin necesidad de programar HTML.",

        "html":"HTML es el lenguaje que define la estructura de una página web mediante etiquetas.",

        "css":"CSS sirve para dar estilo a una página web, modificando colores, tamaños, fuentes y distribución.",

        "java":"Java es un lenguaje orientado a objetos utilizado para aplicaciones empresariales y Android.",

        "sql":"SQL permite crear, consultar y modificar bases de datos.",

        "base de datos":"Una base de datos organiza información para almacenarla y consultarla eficientemente.",

        "redes":"Las redes permiten que diferentes dispositivos compartan información y recursos mediante protocolos de comunicación.",

        "ciberseguridad":"La ciberseguridad protege sistemas, redes y datos contra accesos no autorizados y ataques informáticos.",

        "algoritmo":"Un algoritmo es una secuencia ordenada de pasos para resolver un problema.",

        "programación":"La programación consiste en crear instrucciones para que una computadora realice tareas específicas.",

        "git":"Git es un sistema de control de versiones que registra los cambios realizados en un proyecto.",

        "github":"GitHub es una plataforma para almacenar repositorios Git y colaborar con otros desarrolladores.",

        "inteligencia artificial":"La inteligencia artificial desarrolla sistemas capaces de aprender, analizar información y tomar decisiones basadas en datos."
    }

    for palabra, respuesta in respuestas.items():
        if palabra in t:
            return respuesta

    if "gracias" in t:
        return "¡Con gusto! Estoy aquí para ayudarte."

    if "adios" in t or "adiós" in t or "bye" in t:
        return "¡Hasta luego! Fue un gusto ayudarte."

    if "quien eres" in t or "quién eres" in t:
        return "Soy Carlos Tutor Virtual 2.0, un asistente creado con Streamlit para responder preguntas básicas sobre informática."

    if "como estas" in t or "cómo estás" in t:
        return "Estoy funcionando correctamente y listo para ayudarte."

    return (
        "Aún soy una versión educativa del ChatBot 2.0. "
        "Actualmente puedo responder preguntas sobre Python, Streamlit, HTML, CSS, Java, SQL, redes, algoritmos, Git, GitHub, bases de datos, ciberseguridad e inteligencia artificial."
    )

# ---------- Entrada ----------
prompt = st.chat_input("Escribe tu pregunta...")

if pregunta:
    prompt = pregunta

# ---------- Procesamiento ----------
if prompt:

    hora = datetime.now().strftime("%H:%M")

    st.session_state.messages.append({
        "role":"user",
        "content":prompt,
        "hora":hora
    })

    st.session_state.contador += 1

    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(hora)

    with st.chat_message("assistant"):

        with st.spinner("Carlos está escribiendo..."):
            time.sleep(1)

        respuesta = responder(prompt)

        st.markdown(respuesta)
        st.caption(hora)

    st.session_state.messages.append({
        "role":"assistant",
        "content":respuesta,
        "hora":hora
    })

    st.session_state.contador += 1
