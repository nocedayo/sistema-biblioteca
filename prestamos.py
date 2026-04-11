from conexion import conectar

def registrar_prestamo(libro_id, socio_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO prestamos (libro_id, socio_id) VALUES (%s, %s)",
        (libro_id, socio_id)
    )
    cursor.execute(
        "UPDATE libros SET disponible = FALSE WHERE id = %s",
        (libro_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Préstamo registrado correctamente!")

def registrar_devolucion(libro_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE prestamos SET activo = FALSE, fecha_devolucion = CURRENT_DATE WHERE libro_id = %s AND activo = TRUE",
        (libro_id,)
    )
    cursor.execute(
        "UPDATE libros SET disponible = TRUE WHERE id = %s",
        (libro_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Devolución registrada correctamente!")

def ver_prestamos_activos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.id, l.titulo, s.nombre, p.fecha_prestamo
        FROM prestamos p
        JOIN libros l ON p.libro_id = l.id
        JOIN socios s ON p.socio_id = s.id
        WHERE p.activo = TRUE
    """)
    prestamos = cursor.fetchall()
    cursor.close()
    conn.close()

    if not prestamos:
        print("No hay préstamos activos.")
    else:
        print("\n📋 PRÉSTAMOS ACTIVOS:")
        print("-" * 50)
        for p in prestamos:
            print(f"ID: {p[0]} | {p[1]} → {p[2]} | Desde: {p[3]}")

# Probar
if __name__ == "__main__":
    registrar_prestamo(1, 1)
    ver_prestamos_activos()