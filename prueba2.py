import csv
import cv2
import face_recognition


# Listas para almacenar las codificaciones y los nombres
rostros_conocidos = []
nombres = []

# Leer el archivo CSV
with open('rostros_conocidos.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la primera fila (encabezados)

    for row in reader:
        codificacion = row[0]
        nombre = row[1]

        # Convertir la codificación de cadena a lista
        codificacion = [float(num) for num in codificacion[1:-1].split(', ')]

        rostros_conocidos.append(codificacion)
        nombres.append(nombre)

print("Se han leído las codificaciones y los nombres desde el archivo CSV.")



# ------------ inicio de deteccion ----------------------------------------------


# Redimensionar imagen test

nuevo_ancho = 800
nuevo_alto = 800


imgTest = cv2.imread("daniel.jpg")

image_redimensionada_test = cv2.resize(imgTest, (nuevo_ancho, nuevo_alto))

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



"""
# Imprimir las codificaciones y los nombres



print("Codificaciones:")
i = 0
for codificacion in rostros_conocidos:
    print(codificacion)
    print(nombres[i])
    i += 1

"""


    
