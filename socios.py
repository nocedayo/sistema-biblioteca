from conexion import conectar

def agregar_socio(nombre, dni, email):
    conn = conectar()
    cursor = conn.cursor()
    
    # Verificar si el DNI ya existe
    cursor.execute("SELECT id FROM socios WHERE dni = %s", (dni,))
    existe = cursor.fetchone()
    
    if existe:
        print(f"❌ Ya existe un socio con el DNI {dni}.")
        cursor.close()
        conn.close()
        return
    
    cursor.execute(
        "INSERT INTO socios (nombre, dni, email) VALUES (%s, %s, %s)",
        (nombre, dni, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Socio '{nombre}' agregado correctamente!")

def ver_socios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, dni, email FROM socios")
    socios = cursor.fetchall()
    cursor.close()
    conn.close()

    if not socios:
        print("No hay socios registrados.")
    else:
        print("\n👤 SOCIOS REGISTRADOS:")
        print("-" * 50)
        for socio in socios:
            print(f"ID: {socio[0]} | {socio[1]} | DNI: {socio[2]} | {socio[3]}")

# Probar
if __name__ == "__main__":
    agregar_socio("Ana García", "12345678", "ana@email.com")
    agregar_socio("Juan Pérez", "87654321", "juan@email.com")
    ver_socios()