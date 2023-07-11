import cv2

def abrir_camara():
    # Crea un objeto de captura de video
    cap = cv2.VideoCapture(1)

    # Verifica si la cámara está abierta correctamente
    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    # Lee y muestra el video en un bucle
    while True:
        # Lee un cuadro de video
        ret, frame = cap.read()

        # Si la lectura del cuadro es exitosa, muestra la imagen en una ventana
        if ret:
            cv2.imshow("Cámara", frame)

        # Espera 1 milisegundo y verifica si se presionó la tecla 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera los recursos y cierra la ventana
    cap.release()
    cv2.destroyAllWindows()

# Llama a la función para abrir la cámara
abrir_camara()
