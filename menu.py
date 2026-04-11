from libros import agregar_libro, ver_libros
from socios import agregar_socio, ver_socios
from prestamos import registrar_prestamo, registrar_devolucion, ver_prestamos_activos

def menu():
    while True:
        print("\n=== 📚 BIBLIOTECA ===")
        print("1. Ver libros")
        print("2. Agregar libro")
        print("3. Ver socios")
        print("4. Agregar socio")
        print("5. Registrar préstamo")
        print("6. Registrar devolución")
        print("7. Ver préstamos activos")
        print("0. Salir")

        opcion = input("\nElegí una opción: ")

        if opcion == "1":
            ver_libros()
        elif opcion == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            anio = int(input("Año: "))
            agregar_libro(titulo, autor, genero, anio)
        elif opcion == "3":
            ver_socios()
        elif opcion == "4":
            nombre = input("Nombre: ")
            dni = input("DNI: ")
            email = input("Email: ")
            agregar_socio(nombre, dni, email)
        elif opcion == "5":
            ver_libros()
            libro_id = int(input("ID del libro: "))
            ver_socios()
            socio_id = int(input("ID del socio: "))
            registrar_prestamo(libro_id, socio_id)
        elif opcion == "6":
            ver_prestamos_activos()
            libro_id = int(input("ID del libro a devolver: "))
            registrar_devolucion(libro_id)
        elif opcion == "7":
            ver_prestamos_activos()
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    menu()