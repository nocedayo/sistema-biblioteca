import psycopg2
def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="biblioteca",
        user="postgres",
        password="launica"
    )
    return conn
# Probar la conexión
if __name__ == "__main__":
    try:
        conn = conectar()
        print("✅ Conexión exitosa a PostgreSQL!")
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")
