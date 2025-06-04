-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS student_safety_db;
USE student_safety_db;

CREATE TABLE DIRECTRICES (
    id_directrices INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    documento_directriz INT UNIQUE,
    nombres_directriz VARCHAR(200) NOT NULL,
    apellidos_directriz VARCHAR(200) NOT NULL,
    cargo_directriz VARCHAR(200) NOT NULL,
    nota VARCHAR(200) NULL
);

CREATE TABLE GRADO_GRUPO (
    id_grado_grado INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    grado_grupo INT UNIQUE,
    director_id INT NOT NULL,
    FOREIGN KEY (director_id) REFERENCES DIRECTRICES(id_directrices)
);

CREATE TABLE PERSONAS (
    id_personas INT PRIMARY KEY NOT NULL,
    documento_persona INT UNIQUE,
    nombres_persona VARCHAR(200) NOT NULL,
    apellidos_persona VARCHAR(200) NOT NULL,
    tipo_personas ENUM('estudiante','egresado') NOT NULL,
    grado_grupo_id INT,
    FOREIGN KEY (grado_grupo_id) REFERENCES GRADO_GRUPO(id_grado_grado)
);

CREATE TABLE CITA (
    id_cita INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fechaHora_cita TIMESTAMP NOT NULL,
    motivo_cita VARCHAR(200),
    directrizEncargado_id INT,
    personaCitada_id INT NOT NULL,
    FOREIGN KEY (directrizEncargado_id) REFERENCES DIRECTRICES(id_directrices),
    FOREIGN KEY (personaCitada_id) REFERENCES PERSONAS(id_personas)
);

CREATE TABLE ASISTENCIA (
    id_asistencia INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    fechaHora TIMESTAMP NOT NULL,
    persona_id INT NOT NULL,
    FOREIGN KEY (persona_id) REFERENCES PERSONAS(id_personas)
);

