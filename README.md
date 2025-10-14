## STUDENTSAFETS
- ### RUTAS RELEVANTES "No Interfaz":
    - "**/registrar_asistencia**" Ruta para la busqueda de personas en la 'DB' y luego se registra su asistencia.
    - "**/verificar_directriz**"  Ruta donde se verifica la existencia de un documento en el QR, Si el documento pertenece a un directriz. Guarda el nombre completo y devuelve una respuesta JSON:true
    - "**/verificar_clave**" Ruta en donde se valida que el documento ingresado por QR coincide con uno ya existente en la 'BD'

- ### RUTAS RELEVANTES "Interfaz":
    - "**/**" Ruta de inicio, Pagina principal.
    [Inicio]: /
    - "**/escaner**" Control de acceso (asistencia) para estudiantes.
    - "**/admin_qr**" Ruta para acceder al panel de administrador con doble factor de autentificación
    - "**/admin_dashboard**" Ruta para la interfaz del panel de administración, donde un administrador ingresa con su nombre desde el inicio de seccion. puede entrar, seleccionar y luego consultar las asitencias de los grupos en la 'BD'
    - "**/consultar_asistencias**" Lista los grupos recibidos y busca las asistencias de esos grupos en la 'BD'
    - "**/api/grupo**" Ruta "Experimetal" (No interfaz) Menús desplegables
    -"**/generador_qr**" Ruta para registrar estudiantes y directrices nuevos en la 'BD', Generacion de QR personal por primera vez (12/09/2025 => Corregir inserccion en la BD de los estudiantes)
    - "**/reportes_asistencias**" Consulta todo los grados y sus directores y muestra en la interfaz para que el administrador pueda elegir uno y descagar un excel con esta infromacion.


# 🧠 Base de Datos `student_safety_db`

## 📘 Descripción general
La base de datos **`student_safety_db`** fue diseñada para un sistema de control de ingreso y asistencia institucional basado en **códigos QR**, utilizado por estudiantes, egresados y personal administrativo.  
Su objetivo es permitir un **registro automatizado, seguro y verificable** de cada persona que ingresa a la institución, con controles de acceso diferenciados y trazabilidad de las asistencias y citas.

---

## 🧩 Estructura general
La base de datos se compone de cinco tablas principales:

1. `DIRECTRICES`
2. `GRADO_GRUPO`
3. `PERSONAS`
4. `CITA`
5. `ASISTENCIA`

Estas tablas están relacionadas entre sí mediante **claves foráneas**, asegurando integridad referencial y permitiendo una relación jerárquica entre directivos, grupos, estudiantes y sus registros de ingreso.

---

## 🧱 1. Tabla `DIRECTRICES`

**Propósito:**  
Almacena los datos de las directrices o personal administrativo responsable de cada grupo y de la gestión de citas.

**Campos:**
- `id_directrices`: Clave primaria.
- `documento_directriz`: Documento único.
- `nombres_directriz`, `apellidos_directriz`: Datos personales.
- `cargo_directriz`: Rol institucional.
- `nota`: Campo opcional.
- `clave_directriz`: Contraseña del área administrativa.

**Relaciones:**  
Se conecta con `GRADO_GRUPO` y `CITA`.

---

## 🧾 2. Tabla `GRADO_GRUPO`

**Propósito:**  
Define los grupos académicos y los asocia con su directriz.

**Campos:**
- `id_grado_grado`: Clave primaria.
- `grado_grupo`: Identificador del grupo.
- `director_id`: Clave foránea a `DIRECTRICES(id_directrices)`.

**Relación:**  
Una directriz puede dirigir varios grupos (1:N).

---

## 👥 3. Tabla `PERSONAS`

**Propósito:**  
Contiene estudiantes y egresados.

**Campos:**
- `id_personas`: Clave primaria.
- `documento_persona`: Documento único.
- `nombres_persona`, `apellidos_persona`: Datos personales.
- `tipo_personas`: ENUM('estudiante', 'egresado').
- `grado_grupo_id`: FK a `GRADO_GRUPO(id_grado_grado)`.

**Relación:**  
Un grupo puede tener muchos estudiantes, los egresados no requieren grupo.

---

## 📅 4. Tabla `CITA`

**Propósito:**  
Registra las citas entre directrices y personas.

**Campos:**
- `id_cita`: Clave primaria.
- `fechaHora_cita`: Fecha y hora.
- `motivo_cita`: Descripción.
- `directrizEncargado_id`: FK a `DIRECTRICES`.
- `personaCitada_id`: FK a `PERSONAS`.

**Relación:**  
Una directriz puede tener múltiples citas (1:N).

---

## 🕓 5. Tabla `ASISTENCIA`

**Propósito:**  
Registra cada ingreso mediante QR.

**Campos:**
- `id_asistencia`: Clave primaria.
- `fechaHora`: Momento del registro.
- `nombres_asistencia`, `apellidos_asistencia`: Datos del ingreso.
- `persona_id`: FK hacia `PERSONAS(documento_persona)`.

**Observación:**  
La redundancia de nombres acelera las operaciones de inserción.

---

## 🔗 Relaciones entre tablas

| Relación | Tipo | Descripción |
|-----------|------|-------------|
| DIRECTRICES → GRADO_GRUPO | 1:N | Una directriz puede dirigir varios grupos |
| GRADO_GRUPO → PERSONAS | 1:N | Un grupo puede tener muchos estudiantes |
| PERSONAS → ASISTENCIA | 1:N | Una persona puede registrar muchas asistencias |
| DIRECTRICES → CITA | 1:N | Una directriz puede tener muchas citas |
| PERSONAS → CITA | 1:N | Una persona puede tener varias citas |

---

## ⚙️ Consideraciones y mejoras

1. **Redundancia controlada:**  
   `ASISTENCIA` repite nombres por eficiencia y seguridad.

2. **Posibles mejoras:**  
   - Usar UUIDs.  
   - Tabla `USUARIOS` para unificar tipos.  
   - Tabla `ROL` para permisos.  
   - Índices en `documento_persona` y `fechaHora`.

---

## 🧾 Conclusión
La base de datos **`student_safety_db`** mantiene un equilibrio entre normalización y eficiencia.  
Soporta adecuadamente las funciones del sistema: control de acceso, trazabilidad y validación segura mediante QR y credenciales.

