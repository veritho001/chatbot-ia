import streamlit as st
import time
from datetime import datetime

# ================= CONFIGURACIÓN =================

st.set_page_config(
    page_title="Carlos Tutor Virtual 2.0",
    page_icon="🤖",
    layout="centered"
)

# ================= ESTILOS =================

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
.stSidebar{
    background:#f8f9fa;
}
.tema{
    background:#eef3ff;
    padding:8px;
    border-radius:8px;
    margin-bottom:6px;
}
.footer{
    text-align:center;
    color:gray;
    font-size:12px;
}
</style>
""", unsafe_allow_html=True)

# ================= ESTADO =================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "contador" not in st.session_state:
    st.session_state.contador = 0

# ================= BARRA LATERAL =================

with st.sidebar:

    st.title("🤖 Carlos 2.0")
    st.caption("Tutor Virtual")

    st.markdown("### Estado")
    st.write(f"💬 Mensajes: {st.session_state.contador}")

    st.markdown("---")

    st.markdown("### 📚 Temas de Informática")

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

    st.markdown("### 🩺 Primeros Auxilios")

    st.markdown("""
    Preguntas disponibles:

    - Me duele la cabeza
    - Me duele el estómago
    - Tengo fiebre
    - Tengo tos
    - Tengo dolor de garganta
    - Me siento mareado
    - Tengo náuseas
    - Me hice una cortadura
    - Tengo una quemadura
    """)

    st.markdown("---")

    if st.button("🗑️ Limpiar conversación", use_container_width=True):
        st.session_state.messages = []
        st.session_state.contador = 0
        st.rerun()

# ================= ENCABEZADO =================

st.title("🤖 Carlos Tutor Virtual 2.0")
st.caption("Asistente de informática y orientación básica de primeros auxilios.")

st.info(
    "Puedes preguntarme sobre programación, redes, bases de datos o recibir orientación básica sobre algunos síntomas comunes."
)

# ================= BOTONES RÁPIDOS =================

st.markdown("### Preguntas rápidas")

col1, col2, col3 = st.columns(3)

pregunta = None

with col1:
    if st.button("🐍 Python"):
        pregunta = "¿Qué es Python?"

with col2:
    if st.button("💻 Git"):
        pregunta = "¿Qué es Git?"

with col3:
    if st.button("🩺 Dolor de cabeza"):
        pregunta = "Me duele la cabeza"

# ================= MOSTRAR HISTORIAL =================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "hora" in msg:
            st.caption(msg["hora"])

# ================= RESPUESTAS =================

def responder(texto):

    t = texto.lower()
    emergencia = False

    respuestas = {

        "hola":
        "¡Hola! Soy Carlos, tu tutor virtual. ¿En qué puedo ayudarte?",

        "python":
        "Python es un lenguaje de programación muy utilizado para desarrollar aplicaciones, automatizar tareas, crear inteligencia artificial y analizar datos.",

        "streamlit":
        "Streamlit es un framework de Python que permite crear aplicaciones web interactivas sin necesidad de programar HTML.",

        "html":
        "HTML es el lenguaje que define la estructura de una página web mediante etiquetas.",

        "css":
        "CSS sirve para dar estilo a una página web modificando colores, fuentes y distribución.",

        "java":
        "Java es un lenguaje orientado a objetos ampliamente utilizado en aplicaciones empresariales y Android.",

        "sql":
        "SQL permite crear, consultar y modificar bases de datos.",

        "base de datos":
        "Una base de datos organiza información para almacenarla y consultarla de forma eficiente.",

        "redes":
        "Las redes informáticas permiten que varios dispositivos compartan información y recursos.",

        "ciberseguridad":
        "La ciberseguridad protege sistemas, redes y datos contra accesos no autorizados y ataques informáticos.",

        "algoritmo":
        "Un algoritmo es una secuencia ordenada de pasos para resolver un problema.",

        "programación":
        "La programación consiste en crear instrucciones para que una computadora realice tareas específicas.",

        "git":
        "Git es un sistema de control de versiones que registra los cambios realizados en un proyecto.",

        "github":
        "GitHub es una plataforma para almacenar repositorios Git y colaborar con otros desarrolladores.",

        "inteligencia artificial":
        "La inteligencia artificial desarrolla sistemas capaces de aprender, analizar información y tomar decisiones basadas en datos."
    }

    for palabra, respuesta in respuestas.items():
        if palabra in t:
            return respuesta, emergencia

    # ================= PRIMEROS AUXILIOS =================

    if "me duele la cabeza" in t or "dolor de cabeza" in t or "migraña" in t:
        return (
            "🩺 Un dolor de cabeza puede estar relacionado con estrés, deshidratación o falta de descanso. "
            "Descansa, toma agua y evita esfuerzos innecesarios. "
            "Si aparece de forma repentina e intensa, junto con dificultad para hablar, pérdida de fuerza o confusión, busca atención médica urgente.",
            False
        )

    if "me duele el estómago" in t or "dolor de estómago" in t:
        return (
            "🩺 El dolor de estómago puede tener diferentes causas. Mantente hidratado y evita alimentos pesados. "
            "Si el dolor es muy intenso, hay sangre, fiebre alta o el abdomen está muy rígido, busca atención médica urgente.",
            False
        )

    if "fiebre" in t:
        return (
            "🌡️ Descansa, toma líquidos y controla tu temperatura. "
            "Si supera los 39°C, dura varios días o aparece con dificultad para respirar, busca atención médica.",
            False
        )

    if "tos" in t:
        return (
            "😷 Mantente hidratado y observa tu evolución. "
            "Si aparece dificultad para respirar, dolor intenso en el pecho o sangre al toser, busca atención médica.",
            False
        )

    if "dolor de garganta" in t:
        return (
            "🫖 Puedes aliviar el dolor tomando líquidos tibios y descansando. "
            "Si tienes dificultad para respirar o no puedes tragar saliva, busca atención médica.",
            False
        )

    if "mareo" in t or "mareado" in t:
        return (
            "🩺 Siéntate o recuéstate y evita levantarte rápidamente. "
            "Si el mareo provoca desmayo o viene acompañado de dificultad para hablar o mover una parte del cuerpo, busca ayuda urgente.",
            False
        )

    if "náusea" in t or "nausea" in t or "vómito" in t or "vomito" in t:
        return (
            "🤢 Mantente hidratado con pequeños sorbos de agua. "
            "Si el vómito contiene sangre, es persistente o hay signos de deshidratación intensa, busca atención médica.",
            False
        )

    if "cortadura" in t or "corte" in t:
        return (
            "🩹 Lava la herida con agua limpia, presiona con una gasa para detener el sangrado y cúbrela con un apósito limpio. "
            "Si la herida es profunda o el sangrado no se detiene, busca atención médica.",
            False
        )

    if "quemadura" in t:
        return (
            "🔥 Enfría la quemadura con agua corriente durante unos 20 minutos. "
            "No apliques hielo directamente ni revientes ampollas. "
            "Si es extensa o afecta la cara, manos o genitales, busca atención médica.",
            False
        )

    # ================= EMERGENCIAS =================

    sintomas_graves = [
        "no puedo respirar",
        "dificultad para respirar",
        "dolor fuerte en el pecho",
        "convulsión",
        "convulsion",
        "desmayo",
        "inconsciente",
        "hemorragia",
        "sangrado abundante",
        "accidente grave",
        "no responde",
        "no puedo mover",
        "parálisis",
        "paralisis"
    ]

    for s in sintomas_graves:
        if s in t:
            emergencia = True
            return (
                "🚨 Los síntomas que describes podrían indicar una emergencia médica. "
                "Busca ayuda inmediatamente y llama al 911 si es seguro hacerlo.",
                emergencia
            )

    if "gracias" in t:
        return "😊 ¡Con gusto! Estoy aquí para ayudarte.", False

    if "adiós" in t or "adios" in t or "bye" in t:
        return "👋 ¡Hasta luego! Fue un gusto ayudarte.", False

    if "quién eres" in t or "quien eres" in t:
        return (
            "Soy Carlos Tutor Virtual 2.0, un asistente creado con Streamlit para responder preguntas de informática y brindar orientación básica de primeros auxilios.",
            False
        )

    if "cómo estás" in t or "como estas" in t:
        return "😄 Estoy funcionando correctamente y listo para ayudarte.", False

    return (
        "No encontré una respuesta específica para tu consulta. "
        "Puedo ayudarte con temas de informática, programación y orientación básica de primeros auxilios.",
        False
    )

# ================= ENTRADA =================

prompt = st.chat_input("Escribe tu pregunta...")

if pregunta:
    prompt = pregunta

# ================= PROCESAMIENTO =================

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

    respuesta, emergencia = responder(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Carlos está escribiendo..."):
            time.sleep(1)

        st.markdown(respuesta)
        st.caption(hora)

        if emergencia:
            st.error("🚨 Posible emergencia detectada.")
            st.link_button("📞 Llamar al 911", "tel:911")

    st.session_state.messages.append({
        "role":"assistant",
        "content":respuesta,
        "hora":hora
    })

    st.session_state.contador += 1

# ================= PIE =================

st.markdown("---")
st.markdown(
    "<div class='footer'>Carlos Tutor Virtual 2.0 • Desarrollado con Streamlit</div>",
    unsafe_allow_html=True
)
