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
