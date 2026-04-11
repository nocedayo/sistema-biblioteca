CREATE TABLE libros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(100),
    genero VARCHAR(50),
    anio INTEGER,
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE socios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE,
    email VARCHAR(100)
);

CREATE TABLE prestamos (
    id SERIAL PRIMARY KEY,
    libro_id INTEGER REFERENCES libros(id),
    socio_id INTEGER REFERENCES socios(id),
    fecha_prestamo DATE DEFAULT CURRENT_DATE,
    fecha_devolucion DATE,
    activo BOOLEAN DEFAULT TRUE
);