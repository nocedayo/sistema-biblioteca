from conexion import conectar 

def buscar_tit(tit_libro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio, disponible FROM libros where titulo = %s", (tit_libro,))
    libros = cursor.fetchall()
    cursor.close()
    conn.close()
    if not libros:
        print(f"🔍 No se encontraron libros con el título: '{tit_libro}'")
    else:
        print(f"📖 Resultados para '{tit_libro}':")
        for libro in libros:
            # Desempaquetamos la tupla según el orden del SELECT
            id_l, titulo, autor, anio, disponible = libro
            estado = "✅ Disponible" if disponible else "❌ Prestado"
            
            print(f"ID: {id_l} | Autor: {autor} | Año: {anio} | Estado: {estado}")

    cursor.close()
    conn.close()
#buscar por autor 
def buscar_autor(autor_libro):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, autor, anio, disponible FROM libros where autor = %s", (autor_libro,))
    libros = cursor.fetchall()
    cursor.close()
    conn.close()
    if not libros:
        print(f"🔍No se encontraron libros con el autor: '{autor_libro}'")
    else:
        print(f"📖 Resultados libros con autor:'{autor_libro}':")
        for libro in libros:
            # Desempaquetamos la tupla según el orden del SELECT
            id_l, titulo, autor, anio, disponible = libro
            estado = "✅ Disponible" if disponible else "❌ Prestado"
            
            print(f"ID: {id_l} | Autor: {autor} | Año: {anio} | Estado: {estado}")

    cursor.close()
    conn.close()




if __name__ == "__main__":
   buscar_tit("El Principito")
   buscar_autor("El Principito")
