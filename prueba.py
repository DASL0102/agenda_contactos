import csv
import cv2
import face_recognition

nuevo_ancho = 800
nuevo_alto = 800

imgTest = cv2.imread("3.jpg")
image_redimensionada_test = cv2.resize(imgTest, (nuevo_ancho, nuevo_alto))

ruta_imagenes = ['elonk.jpg','gates.jpg','mark.jpg','daniel.jpg']
nombres = ['Elonk Musk','Bill Gates','Mark Zuckerberg','Daniel Sanchez']

# Cargar rostros conocidos
rostros_conocidos = []

for el in ruta_imagenes:
    imagen = face_recognition.load_image_file(el)
    codificacion = face_recognition.face_encodings(imagen)[0]
    rostros_conocidos.append(codificacion)

# Crear una lista para almacenar las codificaciones y los nombres
codificaciones_nombres = []

face_locations = face_recognition.face_locations(image_redimensionada_test)
face_encodings = face_recognition.face_encodings(image_redimensionada_test, face_locations)

indice = 0
for el in face_encodings:
    nombre = nombres[indice]
    codificaciones_nombres.append([el.tolist(), nombre])
    print(indice)
    indice += 1




# Guardar las codificaciones y los nombres en un archivo CSV
with open('rostros_conocidos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Codificación', 'Nombre'])
    writer.writerows(codificaciones_nombres)

print("Las codificaciones y los nombres se han guardado correctamente en el archivo CSV.")
