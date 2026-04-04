from conexion import conectar

def agregar_libro(titulo, autor, genero, anio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO libros (titulo, autor, genero, anio) VALUES (%s, %s, %s, %s)",
        (titulo, autor, genero, anio)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Libro '{titulo}' agregado correctamente!")

def ver_libros():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio, disponible FROM libros")
    libros = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not libros:
        print("No hay libros registrados.")
    else:
        print("\n📚 LIBROS EN LA BIBLIOTECA:")
        print("-" * 50)
        for libro in libros:
            estado = "✅ Disponible" if libro[4] else "❌ Prestado"
            print(f"ID: {libro[0]} | {libro[1]} - {libro[2]} ({libro[3]}) | {estado}")

# Probar
if __name__ == "__main__":
    agregar_libro("Cien años de soledad", "García Márquez", "Novela", 1967)
    agregar_libro("El Aleph", "Borges", "Cuento", 1949)
    ver_libros()