CREATE TABLE usuarios (
    id INT SERIAL PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    rol VARCHAR(10) NOT NULL,
    constraseña VARCHAR(15) NOT NULL
); 

CREATE TABLE clientes (
    id INT SERIAL PRIMARY KEY,
    nombre VARCHAR(25) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    telefono VARCHAR,
    fecha_alta DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_vencimiento DATE NOT NULL,
    usuario_id INT,

    CONSTRAINT fk_usuario
        FOREIGN KEY(usuario_id)
        REFERENCES usuarios(id) 
        ON DELETE SET NULL
);

CREATE TABLE membresias (
    id INT SERIAL PRIMARY KEY,
    nombre VARCHAR(10) NOT NULL,
    duracion_dias INT NOT NULL,
    precio FLOAT NOT NULL
);

CREATE TABLE pagos (
    id INT SERIAL PRIMARY KEY,
    fecha_pago DATE NOT NULL DEFAULT CURRENT_DATE,
    cliente_id INT,
    membresia_id INT,
    usuario_id INT,

    CONSTRAINT fk_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
        ON DELETE SET NULL,
    
    CONSTRAINT fk_membresia
        FOREIGN KEY (membresia_id)
        REFERENCES membresias(id)
        ON DELETE SET NULL,

    CONSTRAINT fk_usuario
        FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE SET NULL
);