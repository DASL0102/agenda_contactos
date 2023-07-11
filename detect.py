import cv2
import face_recognition

# Ruta al archivo de video
ruta_video = "video.mp4"

# Rutas a las imágenes de rostros conocidos y sus nombres correspondientes
ruta_imagenes = ['mark.jpg', "gates.jpg","daniel.jpg"]
nombres = ["Mark Zuckerberg", "Bill Gates","Daniel Sanchez"]

# Cargar las imágenes de rostros conocidos y sus codificaciones
rostros_conocidos = []
for ruta_imagen in ruta_imagenes:
    imagen = face_recognition.load_image_file(ruta_imagen)
    codificacion = face_recognition.face_encodings(imagen)[0]
    rostros_conocidos.append(codificacion)

# Abrir el video
cap = cv2.VideoCapture(1)

# Verificar si el video se abrió correctamente
if not cap.isOpened():
    print("No se pudo abrir el video.")
    exit()

# Leer y procesar los frames del video
while True:
    
    ret, frame = cap.read()

    # Si no se pudo leer el frame, se llegó al final del video
    if not ret:
        break

    # Redimensionar el frame
    # frame = cv2.resize(frame, (nuevo_ancho, nuevo_alto))

    # Detectar las ubicaciones de las caras en el frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Recorrer todas las caras detectadas en el frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparar el rostro detectado con los rostros conocidos
        resultados = face_recognition.compare_faces(rostros_conocidos, face_encoding)
        nombre = "Desconocido"

        # Si hay alguna coincidencia, obtener el nombre correspondiente
        if True in resultados:
            indice = resultados.index(True)
            nombre = nombres[indice]

        # Dibujar un rectángulo alrededor de la cara detectada
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Escribir el nombre de la persona sobre el rectángulo
        cv2.putText(frame, nombre, (left, top - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Mostrar el frame con las caras detectadas
    cv2.imshow("Video", frame)

    # Si se presiona la tecla 'q', salir del bucle
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
