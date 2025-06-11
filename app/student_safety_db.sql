-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS student_safety_db;
USE student_safety_db;

CREATE TABLE DIRECTRICES (
    id_directrices INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    documento_directriz INT UNIQUE,
    nombres_directriz VARCHAR(200) NOT NULL,
    apellidos_directriz VARCHAR(200) NOT NULL,
    cargo_directriz VARCHAR(200) NOT NULL,
    nota VARCHAR(200) NULL,
    clave_directriz VARCHAR(255) NOT NULL
);

CREATE TABLE GRADO_GRUPO (
    id_grado_grado INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    grado_grupo INT UNIQUE,
    director_id INT NOT NULL,
    FOREIGN KEY (director_id) REFERENCES DIRECTRICES(id_directrices)
);

CREATE TABLE PERSONAS (
    id_personas INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
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
    nombres_asistencia VARCHAR(200) NOT NULL,
    apellidos_asistencia VARCHAR(200) NOT NULL,
    persona_id INT NOT NULL,
    FOREIGN KEY (persona_id) REFERENCES PERSONAS(documento_persona)
);

-- Uso de la base de datos
USE student_safety_db;

-- Inserciones en DIRECTRICES
INSERT INTO DIRECTRICES (documento_directriz, nombres_directriz, apellidos_directriz, cargo_directriz, nota, clave_directriz) VALUES
(1001, 'Carlos', 'Martínez', 'Director General', 'Responsable del plantel', 'clave123'),
(1002, 'Lucía', 'Gómez', 'Coordinadora Académica', NULL, 'clave456'),
(1003, 'Roberto', 'Pérez', 'Orientador Escolar', 'Encargado de bienestar estudiantil', 'clave789'),
(1004, 'Ana', 'Sánchez', 'Director de Seguridad', NULL, 'clave321'),
(1005, 'Luis', 'Torres', 'Jefe de Disciplina', 'Encargado de sanciones', 'clave654'),
(1006, 'María', 'Ramírez', 'Coordinadora de Grados', NULL, 'clave987'),
(1007, 'Javier', 'Díaz', 'Subdirector Académico', NULL, 'clave147'),
(1008, 'Paola', 'Morales', 'Psicóloga Institucional', 'Atención psicológica', 'clave258'),
(1009, 'Esteban', 'Cruz', 'Inspector General', NULL, 'clave369'),
(1010, 'Sofía', 'Vargas', 'Orientadora Vocacional', NULL, 'clave159');

-- Inserciones en GRADO_GRUPO
INSERT INTO GRADO_GRUPO (grado_grupo, director_id) VALUES
(601, 1),
(602, 2),
(701, 3),
(702, 4),
(801, 5),
(802, 6),
(901, 7),
(902, 8),
(1001, 9),
(1002, 10);

-- Inserciones en PERSONAS
INSERT INTO PERSONAS (documento_persona, nombres_persona, apellidos_persona, tipo_personas, grado_grupo_id) VALUES
(2001, 'Juan', 'López', 'estudiante', 1),
(2002, 'Camila', 'Rodríguez', 'estudiante', 1),
(2003, 'Andrés', 'García', 'estudiante', 2),
(2004, 'Santiago', 'Hernández', 'estudiante', 2),
(2005, 'Valentina', 'Ruiz', 'estudiante', 3),
(2006, 'Mariana', 'Flores', 'estudiante', 4),
(2007, 'Sebastián', 'Jiménez', 'estudiante', 5),
(2008, 'Mateo', 'Paredes', 'egresado', 6),
(2009, 'Isabella', 'Castillo', 'egresado', 7),
(2010, 'Daniel', 'Gutiérrez', 'egresado', 8);

-- Inserciones en CITA
INSERT INTO CITA (fechaHora_cita, motivo_cita, directrizEncargado_id, personaCitada_id) VALUES
('2025-06-11 09:00:00', 'Reunión de seguimiento académico', 1, 1),
('2025-06-11 10:00:00', 'Orientación psicológica', 8, 2),
('2025-06-12 08:30:00', 'Reporte disciplinario', 5, 3),
('2025-06-12 11:00:00', 'Reunión con padres de familia', 2, 4),
('2025-06-13 09:15:00', 'Consulta vocacional', 10, 5),
('2025-06-13 10:45:00', 'Evaluación de desempeño', 3, 6),
('2025-06-14 09:00:00', 'Orientación de egreso', 7, 7),
('2025-06-14 11:30:00', 'Seguimiento de exalumnos', 9, 8),
('2025-06-15 08:00:00', 'Charla de seguridad', 4, 9),
('2025-06-15 10:00:00', 'Asesoría de proyecto', 6, 10);

-- Inserciones en ASISTENCIA
INSERT INTO ASISTENCIA (fechaHora, nombres_asistencia, apellidos_asistencia, persona_id) VALUES
('2025-06-10 07:00:00', 'Juan', 'López', 2001),
('2025-06-10 07:00:00', 'Camila', 'Rodríguez', 2002),
('2025-06-10 07:00:00', 'Andrés', 'García', 2003),
('2025-06-10 07:00:00', 'Santiago', 'Hernández', 2004),
('2025-06-10 07:00:00', 'Valentina', 'Ruiz', 2005),
('2025-06-10 07:00:00', 'Mariana', 'Flores', 2006),
('2025-06-10 07:00:00', 'Sebastián', 'Jiménez', 2007),
('2025-06-10 07:00:00', 'Mateo', 'Paredes', 2008),
('2025-06-10 07:00:00', 'Isabella', 'Castillo', 2009),
('2025-06-10 07:00:00', 'Daniel', 'Gutiérrez', 2010);
