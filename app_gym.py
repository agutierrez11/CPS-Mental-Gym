import streamlit as st
import json
import time

# ==============================================================================
# CONFIGURACIÓN PÁGINA: CPS MENTAL GYM & SYSTEMS THINKING
# ==============================================================================
st.set_page_config(
    page_title="CPS & Mental Models Gym",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background-color: #0b0f19; color: #f3f4f6; }
    .stMetric { background-color: #111827; border: 1px solid #1f2937; border-radius: 10px; padding: 15px; }
    .gym-card { background-color: #1e293b; border: 1px solid #334155; padding: 20px; border-radius: 12px; margin-bottom: 15px; }
    .socratic-card { background-color: #1e1b4b; border-left: 5px solid #6366f1; padding: 18px; border-radius: 10px; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 CPS & Systems Thinking Mental Gym")
st.caption("Gimnasio Agnóstico de Modelos Mentales, Ciencias de la Complejidad & Rebotadero Socrático")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🏛️ Marcos Mentales (Untools)", "🔄 Simulador Cynefin & CPS", "🎙️ Rebotadero Socrático"])

# ==============================================================================
# TAB 1: UNTOOLS & MARCOS MENTALES
# ==============================================================================
with tab1:
    st.subheader("🛠️ Untools: Modelos Mentales para la Toma de Decisiones")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="gym-card">
            <h4>🧊 1. El Modelo del Iceberg (Systems Thinking)</h4>
            <p><b>Superficie:</b> Eventos visibles (Lo que sucede ahora).</p>
            <p><b>Capa Media:</b> Patrones y tendencias a lo largo del tiempo.</p>
            <p><b>Capa Profunda:</b> Estructuras sistémicas y bucles de retroalimentación.</p>
            <p><b>Raíz:</b> Modelos mentales y creencias culturales no cuestionadas.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="gym-card">
            <h4>🔄 2. Inversion Thinking (Inversión)</h4>
            <p>En lugar de intentar descifrar cómo tener éxito, identifica exactamente cómo garantizar el fracaso absoluto y elimina esas conductas del sistema.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="gym-card">
            <h4>🧱 3. First Principles Thinking (Primeros Principios)</h4>
            <p>Descompón un problema complejo en sus verdades fundamentales más básicas e innegables. Construye la solución desde cero sin razonar por analogía.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="gym-card">
            <h4>⚖️ 4. Second-Order Thinking (Pensamiento de 2° Orden)</h4>
            <p>Pregúntate siempre: <i>"¿Y luego qué?"</i>. Evalúa las consecuencias de las consecuencias a 6, 12 y 36 meses.</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: SIMULADOR CYNEFIN
# ==============================================================================
with tab2:
    st.subheader("🧩 Clasificador del Framework Cynefin (Dave Snowden)")
    
    problem_input = st.text_area("Describe el problema o dilema que estás analizando:", height=100)
    
    if st.button("🚀 Diagnosticar Dominio Cynefin", type="primary"):
        with st.spinner("Analizando dinámica de sistemas..."):
            time.sleep(0.4)
            st.markdown("""
            <div class="socratic-card">
                <h4>🔮 DIAGNÓSTICO SUGERIDO: ZONA COMPLEJA</h4>
                <p><b>Mecánica:</b> Las causas y efectos no son proporcionales ni obvias en tiempo real.</p>
                <p><b>Estrategia Recomendada:</b> <code>Probe ──► Sense ──► Respond</code> (Experimento de bajo riesgo para recibir retroalimentación del sistema).</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 3: REBOTADERO SOCRÁTICO
# ==============================================================================
with tab3:
    st.subheader("🎙️ Rebotadero Socrático de Ideas")
    st.info("Ingresa una hipótesis para recibir 2 preguntas de fricción socrática y desafiar tus supuestos.")
    
    user_idea = st.text_input("Ingresa tu idea o premisa:")
    if st.button("❓ Rebotar Premisa"):
        if user_idea:
            st.markdown(f"""
            <div class="socratic-card">
                <h4>❓ PREGUNTAS SOCRÁTICAS DE FRICCIÓN:</h4>
                <p><b>1.</b> ¿Qué evidencia concreta tienes de que la causa raíz es esa y no un síntoma de un modelo mental obsoleto?</p>
                <p><b>2.</b> Si tu premisa sobre <i>"{user_idea}"</i> fuera completamente falsa, ¿cuál sería la alternativa más lógica que estás ignorando por sesgo de confirmación?</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("CPS & Mental Models Gym • Agnóstico de Marca • LightRAG & Systems Thinking Powered")
