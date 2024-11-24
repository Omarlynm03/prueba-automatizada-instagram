# Historias de Usuario

## Historia de Usuario 1: Inicio de Sesión
**Descripción:**  
Como usuario de Instagram, quiero iniciar sesión con mi nombre de usuario y contraseña para acceder a mi cuenta.

**Criterios de Aceptación:**
1. El usuario puede ingresar un nombre de usuario y contraseña válidos.
2. Al hacer clic en "Iniciar sesión", el sistema autentica las credenciales y redirige al feed.

**Criterios de Rechazo:**
1. Si las credenciales son incorrectas, debe aparecer un mensaje de error: *"Usuario o contraseña incorrectos."*
2. Si algún campo está vacío, debe aparecer un mensaje: *"Por favor complete todos los campos."*

---

## Historia de Usuario 2: Publicar una Foto
**Descripción:**  
Como usuario de Instagram, quiero subir una foto con descripción para compartir momentos con mis seguidores.

**Criterios de Aceptación:**
1. El usuario selecciona una foto desde su dispositivo.
2. Puede añadir una descripción y etiquetas antes de publicar.
3. La publicación aparece en el feed personal y en el de los seguidores.

**Criterios de Rechazo:**
1. Si no se selecciona una foto, el botón "Publicar" está deshabilitado.
2. Si ocurre un error al subir la foto, aparece un mensaje: *"Error al subir la foto. Inténtelo nuevamente."*

---

## Historia de Usuario 3: Buscar Usuarios

**Descripción:**

Como usuario de Instagram, quiero buscar a otros usuarios utilizando su nombre para seguir nuevas cuentas.

**riterios de Aceptación:**
Al escribir en la barra de búsqueda, se muestran sugerencias relevantes.
El usuario puede seleccionar una cuenta y ver su perfil.

**Criterios de Rechazo:**
Si no existen resultados, debe aparecer el mensaje: "No se encontraron usuarios con este nombre."
Si el servidor no responde, aparece un mensaje: "Error al cargar la búsqueda."

**Historia de Usuario 4: Ver Notificaciones**

**Descripción:** 
Como usuario de Instagram, quiero ver mis notificaciones para estar al tanto de las interacciones en mis publicaciones.

**Criterios de Aceptación:**
El usuario puede acceder a una lista de notificaciones desde la barra superior.
Las notificaciones incluyen likes, comentarios, y nuevos seguidores.

**Criterios de Rechazo:**
Si no hay notificaciones, aparece el mensaje: "No tienes nuevas notificaciones."
Si ocurre un error al cargar las notificaciones, aparece un mensaje: "Error al cargar las notificaciones."

**Historia de Usuario 5: Editar Perfil**

**Descripción:**

Como usuario de Instagram, quiero editar mi perfil (nombre, foto, biografía) para actualizar mi información personal.

**Criterios de Aceptación:**

El usuario puede acceder a la configuración del perfil y modificar campos.
Los cambios son guardados y reflejados inmediatamente en el perfil.

**Criterios de Rechazo:**

Si algún campo obligatorio está vacío, aparece el mensaje: "Por favor complete todos los campos obligatorios."
Si ocurre un error al guardar los cambios, aparece un mensaje: "Error al guardar los cambios. Inténtelo nuevamente."