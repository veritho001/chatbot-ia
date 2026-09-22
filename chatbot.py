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
.main{padding-top:1rem;}
.block-container{max-width:900px;}
h1{text-align:center;}
.stSidebar{background:#f8f9fa;}
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
    st.session_state.messages=[]

if "contador" not in st.session_state:
    st.session_state.contador=0

# ================= BARRA LATERAL =================

with st.sidebar:

    st.title("🤖 Carlos 2.0")
    st.caption("Tutor Virtual")

    st.markdown("### Estado")
    st.write(f"💬 Mensajes: {st.session_state.contador}")

    st.markdown("---")

    st.markdown("## 💻 Informática")

    temas=[
        "Python","Streamlit","HTML","CSS","Java",
        "SQL","Git","GitHub","Redes",
        "Ciberseguridad","Base de Datos",
        "Algoritmos","Inteligencia Artificial"
    ]

    for t in temas:
        st.markdown(f"<div class='tema'>📘 {t}</div>",unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 🩺 Salud")

    st.markdown("""
    **Puedes preguntar:**

    - Me duele la cabeza
    - Me duele el estómago
    - Tengo fiebre
    - Tengo tos
    - Tengo dolor de garganta
    - Tengo diarrea
    - Tengo ansiedad
    - Tengo presión alta
    - Me hice una cortadura
    - Tengo una quemadura
    - No puedo respirar
    """)

    st.markdown("---")

    if st.button("🗑️ Limpiar conversación",use_container_width=True):
        st.session_state.messages=[]
        st.session_state.contador=0
        st.rerun()

# ================= ENCABEZADO =================

st.title("🤖 Carlos Tutor Virtual 2.0")
st.caption("Asistente de informática y orientación básica de salud.")

st.info(
    "Puedo responder preguntas sobre programación, tecnología y brindar orientación básica sobre síntomas comunes."
)

# ================= BOTONES RÁPIDOS =================

st.markdown("### Preguntas rápidas")

c1,c2,c3,c4=st.columns(4)

pregunta=None

with c1:
    if st.button("🐍 Python"):
        pregunta="¿Qué es Python?"

with c2:
    if st.button("💻 Git"):
        pregunta="¿Qué es Git?"

with c3:
    if st.button("🤕 Cabeza"):
        pregunta="Me duele la cabeza"

with c4:
    if st.button("🌡️ Fiebre"):
        pregunta="Tengo fiebre"

# ================= HISTORIAL =================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "hora" in msg:
            st.caption(msg["hora"])

# ================= RESPUESTAS =================

def responder(texto):

    t=texto.lower()
    emergencia=False

    # -------- Informática --------

    info={

        "hola":"¡Hola! Soy Carlos, tu tutor virtual. ¿En qué puedo ayudarte?",

        "python":"Python es un lenguaje de programación utilizado para crear aplicaciones, automatizar tareas, desarrollar inteligencia artificial y analizar datos.",

        "streamlit":"Streamlit permite crear aplicaciones web interactivas usando Python de forma sencilla.",

        "html":"HTML define la estructura de una página web mediante etiquetas.",

        "css":"CSS permite dar estilo a una página web.",

        "java":"Java es un lenguaje orientado a objetos utilizado en aplicaciones empresariales y Android.",

        "sql":"SQL permite consultar y administrar bases de datos.",

        "git":"Git es un sistema de control de versiones.",

        "github":"GitHub es una plataforma para almacenar repositorios Git y colaborar en proyectos.",

        "algoritmo":"Un algoritmo es una secuencia ordenada de pasos para resolver un problema.",

        "base de datos":"Una base de datos organiza información para almacenarla y consultarla eficientemente.",

        "redes":"Las redes permiten la comunicación entre dispositivos mediante protocolos.",

        "ciberseguridad":"La ciberseguridad protege sistemas y datos frente a ataques.",

        "inteligencia artificial":"La inteligencia artificial desarrolla sistemas capaces de aprender y tomar decisiones utilizando datos."
    }

    for palabra,respuesta in info.items():
        if palabra in t:
            return respuesta,False

    # -------- Emergencias --------

    graves=[
        "no puedo respirar",
        "dificultad para respirar",
        "dolor fuerte en el pecho",
        "convulsión",
        "convulsion",
        "desmayo",
        "inconsciente",
        "hemorragia",
        "sangrado abundante",
        "no responde",
        "parálisis",
        "paralisis",
        "accidente grave"
    ]

    for s in graves:
        if s in t:
            return(
                "🚨 Los síntomas que describes podrían indicar una emergencia médica. Busca ayuda inmediata y llama al 911.",
                True
            )

    # -------- Salud --------

    sintomas={

        ("dolor de cabeza","me duele la cabeza","migraña"):
        "🤕 El dolor de cabeza puede estar relacionado con estrés, deshidratación o falta de descanso. Descansa, hidrátate y evita el exceso de pantallas. Busca atención urgente si aparece de forma repentina e intensa junto con confusión o dificultad para hablar.",

        ("dolor de estómago","me duele el estómago"):
        "🩺 Mantente hidratado y evita alimentos pesados. Si el dolor es muy intenso, aparece sangre o fiebre alta, consulta de inmediato.",

        ("fiebre",):
        "🌡️ Descansa, toma abundantes líquidos y controla la temperatura. Si supera 39°C o dura varios días, consulta con un profesional.",

        ("tos",):
        "😷 Mantente hidratado y observa si aparece dificultad para respirar o sangre al toser.",

        ("dolor de garganta",):
        "🍵 Los líquidos tibios pueden aliviar el dolor. Consulta si no puedes tragar saliva o respirar correctamente.",

        ("mareo","mareado"):
        "💫 Siéntate o recuéstate. Evita levantarte rápidamente. Si aparece desmayo o dificultad para hablar, busca ayuda urgente.",

        ("náusea","nausea","vómito","vomito"):
        "🤢 Toma pequeños sorbos de agua para evitar la deshidratación. Consulta si el vómito contiene sangre o es persistente.",

        ("diarrea",):
        "💧 Mantente hidratado con agua o suero oral. Consulta si hay sangre o signos de deshidratación.",

        ("estreñimiento",):
        "🥗 Incrementa el consumo de fibra, agua y actividad física.",

        ("dolor de espalda",):
        "🦴 Descansa sin permanecer inmóvil demasiado tiempo y realiza estiramientos suaves.",

        ("dolor de cuello",):
        "🧘 Evita movimientos bruscos y descansa la zona.",

        ("dolor de rodilla",):
        "🦵 Descansa la articulación, aplica hielo durante 15-20 minutos y evita sobrecargarla.",

        ("dolor de hombro",):
        "💪 Descansa el brazo y evita movimientos dolorosos.",

        ("dolor muscular",):
        "🏃 Descansa, hidrátate y realiza estiramientos suaves.",

        ("calambre",):
        "🦵 Estira lentamente el músculo afectado y mantente hidratado.",

        ("quemadura",):
        "🔥 Enfría la quemadura con agua corriente durante unos 20 minutos. No apliques hielo directamente.",

        ("cortadura","corte"):
        "🩹 Lava la herida con agua limpia, presiona para detener el sangrado y cúbrela con un apósito limpio.",

        ("picadura",):
        "🐝 Lava la zona y aplica frío local. Busca ayuda si aparece dificultad para respirar.",

        ("alergia",):
        "🤧 Evita el desencadenante si lo conoces. Busca atención urgente si hay hinchazón en labios o dificultad para respirar.",

        ("resfriado",):
        "🤒 Descansa, hidrátate y controla los síntomas.",

        ("gripe","influenza"):
        "😴 Descansa, toma líquidos y consulta si empeora.",

        ("congestión nasal","nariz tapada"):
        "👃 El lavado nasal con solución salina puede ayudar.",

        ("dolor de oído",):
        "👂 Evita introducir objetos en el oído y consulta si hay secreción.",

        ("conjuntivitis","ojo rojo"):
        "👁️ Lávate las manos con frecuencia y evita compartir toallas.",

        ("insomnio",):
        "🌙 Mantén horarios regulares y reduce el uso de pantallas antes de dormir.",

        ("ansiedad",):
        "🫁 Practica respiraciones lentas y busca apoyo si interfiere con tu vida diaria.",

        ("estrés",):
        "🌿 Descansa, organiza tus actividades y realiza actividad física si puedes.",

        ("hipertensión","presión alta"):
        "❤️ Reduce el consumo de sal y controla tu presión regularmente.",

        ("hipotensión","presión baja"):
        "💧 Levántate lentamente y mantente hidratado.",

        ("asma",):
        "🌬️ Sigue el tratamiento indicado por tu médico y busca ayuda urgente si no puedes respirar bien.",

        ("diabetes",):
        "🩸 Controla tu glucosa siguiendo las indicaciones médicas.",

        ("covid",):
        "🦠 Descansa, mantente hidratado y sigue las recomendaciones sanitarias vigentes.",

        ("embarazo",):
        "🤰 Ante síntomas preocupantes durante el embarazo consulta con un profesional.",

        ("deshidratación",):
        "🚰 Bebe agua o soluciones de rehidratación oral.",

        ("erupción","ronchas"):
        "🌸 Observa si la erupción empeora y consulta si aparece fiebre alta."
    }

    for claves,respuesta in sintomas.items():
        for c in claves:
            if c in t:
                return respuesta,False

    if "gracias" in t:
        return "😊 ¡Con gusto! Estoy aquí para ayudarte.",False

    if "adiós" in t or "adios" in t or "bye" in t:
        return "👋 ¡Hasta luego! Fue un gusto ayudarte.",False

    if "quién eres" in t or "quien eres" in t:
        return(
            "Soy Carlos Tutor Virtual 2.0, un asistente creado con Streamlit para responder preguntas de informática y brindar orientación básica sobre salud.",
            False
        )

    if "cómo estás" in t or "como estas" in t:
        return "😄 Estoy funcionando correctamente y listo para ayudarte.",False

    return(
        "No encontré una respuesta específica para tu consulta. Puedo ayudarte con informática, programación y orientación básica sobre síntomas comunes.",
        False
    )

# ================= ENTRADA =================

prompt=st.chat_input("Escribe tu pregunta...")

if pregunta:
    prompt=pregunta

# ================= CHAT =================

if prompt:

    hora=datetime.now().strftime("%H:%M")

    st.session_state.messages.append({
        "role":"user",
        "content":prompt,
        "hora":hora
    })

    st.session_state.contador+=1

    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(hora)

    respuesta,emergencia=responder(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Carlos está escribiendo..."):
            time.sleep(1)

        st.markdown(respuesta)
        st.caption(hora)

        if emergencia:
            st.error("🚨 Posible emergencia detectada.")
            st.link_button("📞 Llamar al 911","tel:911")

    st.session_state.messages.append({
        "role":"assistant",
        "content":respuesta,
        "hora":hora
    })

    st.session_state.contador+=1

# ================= PIE =================

st.markdown("---")
st.markdown(
    "<div class='footer'>Carlos Tutor Virtual 2.0 • Desarrollado con Streamlit</div>",
    unsafe_allow_html=True
)
