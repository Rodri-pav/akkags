import streamlit as st
import time

# Configuración de la página con estética "Terminal / Hacker"
st.set_page_config(page_title="Birthday OS v1.0", page_icon="💻", layout="centered")

# Estilo CSS personalizado para darle un toque tecnológico/oscuro
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h1, h2, h3 { color: #00FF66 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button {
        background-color: #00FF66; color: black; 
        font-weight: bold; border-radius: 8px;
        border: none; width: 100%;
    }
    .stButton>button:hover { background-color: #00CC52; color: black; }
    div[data-testid="stMarkdownContainer"] { color: #E0E0E0; font-family: 'Courier New', monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("📟 BIRTHDAY_OS v1.0")
st.write("---")

# Inicializamos el estado de la sesión si no existe
if "step" not in st.session_state:
    st.session_state.step = 1

# ==========================================
# PASO 1: EL INICIO (Sobre 1)
# ==========================================
if st.session_state.step == 1:
    st.subheader("🤖 [SISTEMA]: Inicializando protocolo...")
    st.write("¡Felicidades por tus 18 vueltas al sol! Tu itinerario del día ha sido encriptado para garantizar la máxima eficiencia de celebración.")
    st.write("Introduce el código del **Sobre 1** para iniciar la Secuencia.")
    
    codigo_1 = st.text_input("Introduce código de acceso:", key="cod1").strip().upper()
    
    if st.button("Validar Código"):
        if codigo_1 == "START_18":
            with st.spinner("Desencriptando coordenadas..."):
                time.sleep(1.5)
            st.session_state.step = 2
            st.rerun()
        else:
            st.error("❌ CÓDIGO INCORRECTO. Acceso denegado.")

# ==========================================
# PASO 2: EN BUSCA DE NAIARA (Sobre 2)
# ==========================================
elif st.session_state.step == 2:
    st.subheader("📍 [SISTEMA]: Fase 1 Completada")
    st.write("Ubicación alcanzada con éxito. Sin embargo, para procesar la siguiente fase se requiere un hardware externo de máxima confianza.")
    st.info("🔍 Misión: Encuentra a Naiara y pídele el siguiente componente (Sobre 2).")
    
    codigo_2 = st.text_input("Introduce el código de desbloqueo de Naiara:", key="cod2").strip().upper()
    
    if st.button("Conectar Nodo"):
        if codigo_2 == "NAIARA_CONNECT":
            with st.spinner("Sincronizando dispositivos..."):
                time.sleep(1.5)
            st.session_state.step = 3
            st.rerun()
        else:
            st.error("❌ Clave de sincronización errónea.")

# ==========================================
# PASO 3: EL RETO DE LA FOTO (Sobre 3)
# ==========================================
elif st.session_state.step == 3:
    st.subheader("📸 [SISTEMA]: Protocolo de Amistad Detectado")
    st.write("El sistema requiere una prueba visual para verificar la autenticidad del vínculo antes de revelar el destino final.")
    st.write("**Misión:** Haceros una foto grupal (Tú, ella, Naiara y Edgar) y subirla al sistema.")
    
    foto = st.file_uploader("Sube vuestra foto aquí", type=["png", "jpg", "jpeg"])
    
    if foto is not None:
        st.success("✅ Foto recibida correctamente.")
        if st.button("Procesar Datos Finales"):
            with st.spinner("Calculando ruta óptima al destino final..."):
                time.sleep(2.5)
            st.session_state.step = 4
            st.rerun()

# ==========================================
# PASO 4: DESTINO FINAL
# ==========================================
elif st.session_state.step == 4:
    st.balloons()
    st.subheader("🎉 [SUCCESS]: Algoritmo Completado")
    st.write("### ¡TODO LISTO!")
    st.write("El sistema ha calculado que tu fiesta perfecta está completamente preparada.")
    st.write("⚡ **DIRECTIVA FINAL:** Dirigirse de inmediato a las coordenadas de la Base Principal (Casa de mi padre).")
    st.write("¡Prepárate para la sorpresa! 🎂✨")
    
    if st.button("Reiniciar Sistema (Modo Desarrollador)"):
        st.session_state.step = 1
        st.rerun()