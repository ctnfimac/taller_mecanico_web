--DDL
--Script para generar las tablas correspondientes a la base de datos para
--el taller mecánico

-- Tabla WORKSHOP
CREATE TABLE workshop (
    id SERIAL PRIMARY KEY,
    email VARCHAR(30) unique NOT NULL,
    password VARCHAR(100) NOT NULL,
    activated BOOLEAN default true,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- pass: christian
INSERT INTO workshop(email, password, activated, created_at, updated_at)
VALUES('christian@gmail.com', '$2b$12$O1TZuQZEB0a65PBXvManOO3eDA/bWbfVueei2CVNs5cs/B6/ArBWS', true, NOW(), NOW());