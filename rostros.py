import cv2
import face_recognition

nuevo_ancho = 800
nuevo_alto = 800


imgTest = cv2.imread("3.jpg")

image_redimensionada_test = cv2.resize(imgTest, (nuevo_ancho, nuevo_alto))

#ruta de las imagenes
ruta_imagenes = ['elonk.jpg','gates.jpg','mark.jpg','daniel.jpg']
nombres = ['Elonk Musk','Bill Gates','Mark Zuckerberg','Daniel Sanchez']

#cargar rostros conocidos

rostros_conocidos = []

for el in ruta_imagenes:
    imagen = face_recognition.load_image_file(el)  # Carga la imagen
    codificacion = face_recognition.face_encodings(imagen)[0] # Codifica la imagen --- pero averiguar porque e la pos 0
    rostros_conocidos.append(codificacion)





face_locations = face_recognition.face_locations(image_redimensionada_test)
face_encodings = face_recognition.face_encodings(image_redimensionada_test, face_locations)
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Comparar el rostro detectado con los rostros conocidos
        resultados = face_recognition.compare_faces(rostros_conocidos, face_encoding)
        nombre = "Desconocido"

        # Si hay alguna coincidencia, obtener el nombre correspondiente
        if True in resultados:
            indice = resultados.index(True)
            nombre = nombres[indice]

        # Dibujar un rectángulo alrededor de la cara detectada
        cv2.rectangle(image_redimensionada_test, (left, top), (right, bottom), (0, 255, 0), 2)

        # Escribir el nombre de la persona sobre el rectángulo
        cv2.putText(image_redimensionada_test, nombre, (left, top - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Image", image_redimensionada_test)
cv2.waitKey(0)

# Cerrar las ventanas
cap.release()
cv2.destroyAllWindows()




