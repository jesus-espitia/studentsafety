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
    nombres_asistencia VARCHAR(200) NOT NULL,
    apellidos_asistencia VARCHAR(200) NOT NULL,
    persona_id INT NOT NULL,
    FOREIGN KEY (persona_id) REFERENCES PERSONAS(documento_persona)
);


-- Inserciones en DIRECTRICES
INSERT INTO DIRECTRICES (documento_directriz, nombres_directriz, apellidos_directriz, cargo_directriz, nota) VALUES
(1001, 'Laura', 'Gómez', 'Orientadora escolar', 'Psicóloga especializada en adolescentes'),
(1002, 'Carlos', 'Ramírez', 'Jefe de convivencia', 'Encargado de disciplina'),
(1003, 'Marta', 'López', 'Coordinadora académica', 'Supervisa el rendimiento estudiantil'),
(1004, 'Andrés', 'Martínez', 'Rector', 'Dirección general de la institución'),
(1005, 'Ana', 'Castro', 'Psicóloga', 'Atención emocional de los estudiantes'),
(1006, 'Jorge', 'Zapata', 'Inspector', 'Control de ingreso y comportamiento');

-- Inserciones en GRADO_GRUPO
INSERT INTO GRADO_GRUPO (grado_grupo, director_id) VALUES
(601, 1),
(602, 2),
(701, 3),
(702, 4),
(801, 5),
(802, 6);

-- Inserciones en PERSONAS
INSERT INTO PERSONAS (id_personas, documento_persona, nombres_persona, apellidos_persona, tipo_personas, grado_grupo_id) VALUES
(1, 2001, 'María', 'Sánchez', 'estudiante', 1),
(2, 2002, 'Luis', 'Pérez', 'estudiante', 1),
(3, 2003, 'Camila', 'Ríos', 'estudiante', 2),
(4, 2004, 'Juan', 'Torres', 'egresado', NULL),
(5, 2005, 'Sofía', 'Mejía', 'estudiante', 3),
(6, 2006, 'Mateo', 'Díaz', 'egresado', NULL);

-- Inserciones en CITA
INSERT INTO CITA (fechaHora_cita, motivo_cita, directrizEncargado_id, personaCitada_id) VALUES
('2025-06-01 08:00:00', 'Bajo rendimiento académico', 3, 1),
('2025-06-02 10:30:00', 'Conflicto con compañeros', 2, 2),
('2025-06-03 09:15:00', 'Apoyo emocional', 5, 3),
('2025-06-04 11:45:00', 'Seguimiento post-egreso', 1, 4),
('2025-06-05 08:20:00', 'Citación por indisciplina', 6, 5),
('2025-06-06 14:00:00', 'Asesoría vocacional', 5, 6);

-- Inserciones en ASISTENCIA
INSERT INTO ASISTENCIA (fechaHora, nombres_asistencia, apellidos_asistencia, persona_id) VALUES
('2025-06-01 07:50:00', 'María', 'Sánchez', 2001),
('2025-06-01 07:55:00', 'Luis', 'Pérez', 2002),
('2025-06-01 08:00:00', 'Camila', 'Ríos', 2003),
('2025-06-01 08:05:00', 'Juan', 'Torres', 2004),
('2025-06-01 08:10:00', 'Sofía', 'Mejía', 2005),
('2025-06-01 08:15:00', 'Mateo', 'Díaz', 2006);