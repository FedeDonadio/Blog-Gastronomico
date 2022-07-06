# PROYECTO FINAL Donadio Romero Fernandez

BLOG GASTRONOMICO

Hola!

Somos un equipo conformado por: Federico Donadio, Fernando Romero y Federico Fernandez. Pueden encontrar información extra de nosotros en el "Acerca de mi" de nuestro blog.
Para crear el blog, primero nos tuvimos que poner de acuerdo con el tema que nos interesaba. Luego decidimos buscar en Start Bootstrap un tema de blog que nos pareciera interesante. Cuando decidimos los modelos que íbamos a usar, empezamos a desarrollar el proyecto, luego la App.
Se preparó las clases en la carpeta “Models”. Los templates se fueron ajustando, tanto en imágenes, como en los botones para derivar a los otros Html. Se fueron probando las rutas y funciones  de cada template.
Luego empezamos a agregar las clases para los “forms” y así poder cargar en base de datos, información desde los formularios.
Una vez realizado el proyecto base, pasamos a la etapa final de la creacion del Blog, con la implementacion completa de CRUD (Create,Read,Update,Delete), posibilidad de crear usuarios, un login y busqueda por formulario.
A groso modo, las tareas de cada uno fueron las siguientes: 
Federico Fernandez empezó el proyecto, y la app. Creó los modelos, las vistas de las páginas principales, agregó una función para captar error 404 así poder poner un mensaje específico en un template. 
Luego Federico Donadio, hizo la implementación del login, logout, creación de usuarios y la implementación del CRUD de platos. Se encargó de manejar las versiones en Github. También implementó imágenes de fondo para los templates.
Fernando Romero, también trabajó en imágenes y comentarios de los templates, implementó el Login required y finalizó los CRUD de las páginas faltantes.

En la página no son necesarias las rutas de los templates, ya que al ingresar a la misma se podrá navegar mediante la barra de navegación y los vinculos o botones que posee cada página. 
Para poder agregar, borrar o modificar elementos de las distintas páginas será necesario estar logueado. (Si no tiene usuario creado, deberá hacerlo)
Para desloguearse, se deberá pulsar en el nombre de usuario que aparece en la barra de navegacion a la derecha.

Para poder hacer uso del proyecto, descargar el archivo .ZIP.
Una vez descargado, se deberá modificar la ruta de acceso de los Template en el archivo settings.py dentro de la carpeta del proyecto.
La nueva URL a colocar se puede obtener mediante la consola, ubicándose dentro de la carpeta de los templates y escribir “pwd”. 
Para probar la función de captar “error 404” hay que modificar en settings: DEBUG = FALSE Y ALLOWED_HOSTS = [‘*’].

El proyecto se encuentra en la rama "master".

Muchas gracias por visualizar nuestro blog! Esperamos les sea útil y/o les guste.