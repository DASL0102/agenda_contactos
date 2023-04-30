"""  
 Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.
    """

#importamos librerias
import os
import time
from reportlab.pdfgen import canvas

#creamos una agenda
agenda = {}


#añadir contacto
def add_contact():

    name = input(str("Enter name: "))
    phone = input(str("Enter phone number: "))
    mail = input(str("Enter mail direction: "))
    
    new_contact = {"name":name , "phone": phone, "mail": mail}

    if name in agenda:
        contact = agenda[name]
        print("\nExisting contact\n")
        print("Name: ", contact["name"])
        print("Phone number: ", contact["phone"])
        print("mail: ", contact["mail"])
        print("Do you wanna edit this contact? Y/N")
        option = input(str("Enter your selection: "))

        #modificar el contacto
        if(option == "Y" or option == "y"):
            contact["phone"]= input(str("Enter phone number: "))
            contact["mail"]= input(str("Enter mail direction: "))
            agenda[name] = contact

            print(agenda[name])

        
    else:
        agenda[name] = new_contact   #guardamos el nuevo contacto 

# Buscar contacto en agenda
def search_contact():
    name = input(str("Enter name: "))
    if name in agenda:
        contact = agenda[name]
        #mostrar contacto
        print(" Contact Data: \n", "**************\n")
        print("Name: ", contact["name"])
        print("Phone Number: ", contact["phone"])
        print("Mail: ", contact["mail"])
    else:
        print("contact could not be found")  

    option = input("Press 1 to exit: ") 

#Eliminar contacto
def delete_contact():
    name = input(str("Enter name: "))
    if name in agenda:
        del agenda[name]
        print("contact deleted succesfully")
    else:
        print("contact could not be found")

    option = input("Press 1 to exit: ")

#mostrar todos los contactos
def show_AllContacts():
    for key in agenda:
        print(key)

    option = input("Press 1 to exit: ")


#importar a pdf
def contactsToPdf():
    # Crear el archivo PDF
    pdf = canvas.Canvas("agenda.pdf")

    # Insertar los datos en el archivo PDF
    x, y = 50, 750

    for key in agenda:
        contact = agenda[key]

        name = contact["name"]
        phone = contact["phone"]
        mail = contact["mail"]

        pdf.drawString(x, y, "👥: " + name + "📱: " + phone + "📧: " + mail)
        y -= 20
    # Guardar y cerrar el archivo PDF
    pdf.save()


option = 0
while True:
        
    os.system("cls")
    print("  Welcome to diary\n", "*****************")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("5. Import contacs to PDF")
    print("6. Exit")

    option = input("enter your selection: ")

    if option == "1":
        os.system("cls")
        add_contact()
    elif option == "2":
        os.system("cls")
        search_contact()
    elif option == "3":
        os.system("cls")
        delete_contact()
    elif option == "4":
        os.system("cls")
        show_AllContacts()  
    elif option == "5":
        os.system("cls")
        contactsToPdf()               
    elif option == "6":
        os.system("cls")
        break    
    else:
        print("Invalid Option")
        time.sleep(2)
