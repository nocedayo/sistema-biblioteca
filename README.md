# Sistema de Gestión de Biblioteca
Sistema CRUD para gestionar libros, socios y préstamos.

## Tecnologías
- Python 3
- PostgreSQL
- psycopg2

## Archivos
- `conexion.py` — Conexión a la base de datos
- `libros.py` — Gestión de libros
- `socios.py` — Gestión de socios
- `prestamos.py` — Gestión de préstamos
- `menu.py` — Menú principal
- `schema.sql` — Estructura de la base de datos

## Cómo correrlo
1. Instalar PostgreSQL y crear la base de datos con `schema.sql`
2. Instalar dependencias: `pip install psycopg2-binary`
3. Editar `conexion.py` con tu contraseña
4. Ejecutar: `python menu.py`