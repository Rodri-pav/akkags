import cv2
import numpy as np

# El token exacto que contiene el QR de Canva
TOKEN_SECRETO = "CLUB18-VIP-ACCESS-GRANTED"

# Inicializar la webcam (0 suele ser la integrada del portátil)
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

print("||===========================================||")
print("||  CONTROL DE ACCESO: EIGHTEEN • THE CLUB   ||")
print("||         ESPERANDO CÓDIGO QR...            ||")
print("||===========================================||")

while True:
    _, frame = cap.read()
    
    # Invertir el frame para que actúe como un espejo (más cómodo)
    frame = cv2.flip(frame, 1)
    
    # Intentar detectar y decodificar el QR
    data, bbox, _ = detector.detectAndDecode(frame)
    
    # Si detecta un QR con información
    if data:
        # Crear una pantalla de resultado
        pantalla_resultado = np.zeros((400, 700, 3), dtype="uint8")
        
        if data == TOKEN_SECRETO:
            # PANTALLA VERDE: ACCESO CONCEDIDO
            pantalla_resultado[:] = (20, 150, 20) # Color verde de fondo (BGR)
            cv2.putText(pantalla_resultado, "ACCESO CONCEDIDO", (100, 180), 
                        cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 3)
            cv2.putText(pantalla_resultado, "BIENVENIDA AL CLUB", (180, 250), 
                        cv2.FONT_HERSHEY_COMPLEX, 1.0, (200, 255, 200), 2)
            print("🟢 [ENTRADA VÁLIDA]: Acceso Autorizado.")
        else:
            # PANTALLA ROJA: ERROR
            pantalla_resultado[:] = (20, 20, 150) # Color rojo de fondo (BGR)
            cv2.putText(pantalla_resultado, "ACCESO DENEGADO", (120, 180), 
                        cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 255), 3)
            cv2.putText(pantalla_resultado, "ENTRADA INVALIDA", (200, 250), 
                        cv2.FONT_HERSHEY_COMPLEX, 1.0, (200, 200, 255), 2)
            print("🔴 [ALERTA]: Intento de acceso con QR falso.")
            
        # Mostrar la pantalla de resultado durante 5 segundos
        cv2.imshow("CONTROL DE ACCESO VIP", pantalla_resultado)
        cv2.waitKey(5000)
        break

    # Interfaz en vivo de la cámara mientras espera
    # Dibujamos un marco guía en el centro de la pantalla
    height, width, _ = frame.shape
    cv2.rectangle(frame, (int(width/2) - 120, int(height/2) - 120), 
                  (int(width/2) + 120, int(height/2) + 120), (0, 175, 212), 2)
    cv2.putText(frame, "Muestre su PASE VIP aqui", (int(width/2) - 140, int(height/2) - 140), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 175, 212), 2)

    cv2.imshow("SCANNER - EIGHTEEN THE CLUB", frame)
    
    # Si pulsas la tecla 'q', el programa se cierra solo
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()