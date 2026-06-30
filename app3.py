import streamlit as str

# Configuración de la página
str.set_page_config(page_title="Eighteen Club • VIP", page_icon="🎟️", layout="centered")

# Estilos CSS
str.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #f3e5ab; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Playfair Display', serif; }
    div.stButton > button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 20px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Inicializamos el estado del juego si no existe
if 'fase' not in str.session_state:
    str.session_state.fase = 1

str.title("EIGHTEEN • THE CLUB")
str.subheader("VIP Access Management")

# --- FASE 1: INICIO (Pide código del Sobre 1) ---
if str.session_state.fase == 1:
    str.image("images/qr_muy_pixelado.png", caption="PASE VIP: ESTADO BLOQUEADO", width=250)
    str.write("Estimada invitada, su pase está bloqueado. Introduzca el código para iniciar la verificación.")
    
    codigo = str.text_input("Código de Activación:", key="cod1").upper()
    if str.button("Verificar Código"):
        if codigo == "VIP-START":
            str.session_state.fase = 2  # Pasa al radar
            str.rerun()
        else:
            str.error("Código incorrecto. Acceso denegado.")

# --- FASE 2: EL RADAR (Paso Intermedio Nuevo) ---
elif str.session_state.fase == 2:
    str.image("images/qr_muy_pixelado.png", caption="PASE VIP: CONECTANDO AL RADAR...", width=250)
    
    str.warning("📡 RADAR DE PROXIMIDAD ACTIVADO")
    str.write("Buscando la señal del 'Acompañante Autorizado'...")
    
    # Efecto visual de carga/radar
    str.info("📍 SEÑAL DETECTADA EN LAS SIGUIENTES COORDENADAS:")
    
    # AQUÍ PONEMOS EL MAPA: Cambia estas coordenadas por el sitio exacto de Sabadell 
    # donde vaya a estar Naiara (ej: Plaza Sant Roc, un bar, etc.)
    # Coordenadas de ejemplo (Centro de Sabadell): lat=41.546, lon=2.108
    data_mapa = {'lat': [41.524782], 'lon': [2.120393]} 
    str.map(data_mapa, zoom=16)
    
    str.write("Dirígete a la ubicación del mapa. Una vez que hayas localizado físicamente al acompañante, pulsa el botón para proceder.")
    
    if str.button("He localizado a mi acompañante 🟢"):
        str.session_state.fase = 3  # Pasa a la foto
        str.rerun()

# --- FASE 3: CONTROL BIOMÉTRICO (Foto con Naiara) ---
elif str.session_state.fase == 3:
    str.image("images/qr_medio_pixelado.png", caption="PASE VIP: DESENCRIPTANDO... 50%", width=250)
    str.write("¡Contacto autorizado verificado!")
    str.info("Por favor, hágase un selfie con su acompañante y súbalo para confirmar la asistencia grupal.")
    
    foto = str.file_uploader("Subir verificación biométrica", type=["png", "jpg", "jpeg"])
    if foto is not None:
        if str.button("Solicitar Transporte Privado 🚗"):
            str.session_state.fase = 4  # Pasa al QR final
            str.rerun()

# --- FASE 4: ACCESO CONCEDIDO (QR Nítido) ---
elif str.session_state.fase == 4:
    str.balloons()
    str.success("✨ ¡IDENTIDAD VERIFICADA RECONOCIDA! ✨")
    str.image("images/qr_perfecto.png", caption="ACCESO CONCEDIDO", width=250)
    str.write("Muestre este código QR en la pantalla de la entrada del reservado para acceder al evento.")