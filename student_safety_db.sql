-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS student_safety_db;
USE student_safety_db;

-- Tabla principal de usuarios
CREATE TABLE usuarios (
    numero_documento VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    tipo ENUM('estudiante', 'profesor', 'admin') NOT NULL,
    grado VARCHAR(10),             -- Solo estudiantes
    grupo VARCHAR(10),             -- Solo estudiantes
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de egresados
CREATE TABLE egresados (
    numero_documento VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    grado_egresado VARCHAR(10) NOT NULL,
    grupo_egresado VARCHAR(10) NOT NULL,
    año_graduacion INT NOT NULL,
    documento_director_grupo VARCHAR(20),  -- FK a usuarios (profesor)
    contacto VARCHAR(50),                  -- Email o teléfono
    FOREIGN KEY (documento_director_grupo) REFERENCES usuarios(numero_documento)
);

-- Tabla de citas (para egresados)
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento_egresado VARCHAR(20) NOT NULL,
    documento_profesor VARCHAR(20) NOT NULL,
    fecha_cita DATETIME NOT NULL,
    motivo TEXT,
    estado ENUM('pendiente', 'confirmada', 'cancelada') DEFAULT 'pendiente',
    FOREIGN KEY (documento_egresado) REFERENCES egresados(numero_documento),
    FOREIGN KEY (documento_profesor) REFERENCES usuarios(numero_documento)
);

-- Tabla de asistencias (ingreso únicamente)
CREATE TABLE asistencias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    documento_usuario VARCHAR(20) NOT NULL,
    tipo_usuario ENUM('estudiante', 'profesor', 'admin', 'egresado') NOT NULL,
    fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    -- Nota: no se usa FK aquí porque documento puede estar en usuarios o egresados
);
