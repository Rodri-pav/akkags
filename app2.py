import streamlit as str

# Configuración de la página para que parezca una App móvil elegante
str.set_page_config(page_title="Eighteen Club • VIP", page_icon="🎟️", layout="centered")

# Estilos CSS personalizados para poner el fondo oscuro y letras doradas
str.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #f3e5ab; }
    h1, h2, h3 { color: #d4af37 !important; font-family: 'Playfair Display', serif; }
    div.stButton > button { background-color: #d4af37; color: black; font-weight: bold; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Inicializamos el estado del juego si no existe
if 'fase' not in str.session_state:
    str.session_state.fase = 1

str.title("EIGHTEEN • THE CLUB")
str.subheader("VIP Access Management")

# --- FASE 1: INICIO ---
if str.session_state.fase == 1:
    str.image("images/qr_muy_pixelado.png", caption="PASE VIP: ESTADO BLOQUEADO", width=250)
    str.write("Estimada invitada, su pase está retenido. Introduzca el código del Punto de Control 01 para iniciar la verificación.")
    
    codigo = str.text_input("Código de Activación:", key="cod1").upper()
    if str.button("Verificar Código"):
        if codigo == "VIP-START":
            str.session_state.fase = 2
            str.rerun()
        else:
            str.error("Código incorrecto. Acceso denegado.")

# --- FASE 2: CONTROL BIOMÉTRICO ---
elif str.session_state.fase == 2:
    str.image("images/qr_medio_pixelado.png", caption="PASE VIP: DESENCRIPTANDO... 50%", width=250)
    str.write("¡Contacto autorizado verificado! Punto de Control 02: Control Biométrico.")
    str.info("Por favor, hágase un selfie con su acompañante (Naiara) y súbalo para confirmar la asistencia.")
    
    foto = str.file_uploader("Subir instantánea biométrica", type=["png", "jpg", "jpeg"])
    if foto is not None:
        if str.button("Solicitar Transporte Privado"):
            str.session_state.fase = 3
            str.rerun()

# --- FASE 3: ACCESO CONCEDIDO (En app2.py) ---
elif str.session_state.fase == 3:
    str.balloons()
    str.success("✨ ¡IDENTIDAD VERIFICADA Y RECONOCIDA! ✨")
    # Esta imagen contiene el QR real con el texto "CLUB18-VIP-ACCESS-GRANTED"
    str.image("images/qr_perfecto.png", caption="PASE VIP ACTIVADO", width=250)
    str.write("Muestre este código QR en la cámara de la entrada para acceder al reservado.")