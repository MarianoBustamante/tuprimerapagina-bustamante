# tuprimerapagina-bustamante

## Funcionalidades y Orden de Pruebas

1. **Agregar Escritor**
   - **URL:** `/nuevo_escritor/`
   - **Descripción:** Permite agregar un nuevo escritor al sistema.
   - **Pasos para probar:**
     - Accede a la URL directamente o haz clic en "Agregar Escritor" en el menú de navegación.
     - Completa el formulario con el nombre y correo electrónico.
     - Haz clic en "Guardar" para añadir el escritor a la base de datos.

2. **Agregar Tema**
   - **URL:** `/nuevo_tema/`
   - **Descripción:** Permite crear un nuevo tema para clasificar las entradas.
   - **Pasos para probar:**
     - Accede a la URL o selecciona "Agregar Tema" en el menú.
     - Rellena el formulario con el nombre del tema.
     - Presiona "Guardar" para registrar el tema.

3. **Agregar Entrada**
   - **URL:** `/nueva_entrada/`
   - **Descripción:** Permite crear una nueva entrada del blog, asociándola a un escritor y a un tema.
   - **Pasos para probar:**
     - Ingresa a la URL o haz clic en "Mi Diario" en el menú (redirecciona a "nueva entrada").
     - Completa el formulario con título, contenido y selecciona un escritor y un tema previamente creados.
     - Haz clic en "Guardar" para publicar la entrada.

4. **Buscar Entrada**
   - **URL:** `/buscar/`
   - **Descripción:** Permite buscar entradas de blog por el título.
   - **Pasos para probar:**
     - Accede a la URL o selecciona "Buscar Entrada" en el menú.
     - Introduce un título (o parte del mismo) en el campo de búsqueda.
     - Haz clic en "Buscar" y revisa la lista de resultados que aparecen debajo del formulario.

## Instrucciones para Probar el Proyecto

    -en consola:
        git clone https://github.com/MarianoBustamante/tuprimerapagina-bustamante.git
        crea el entorno virtual: "python -m venv venv" y activalo "source venv/scripts/activate"
    -en consola:
        pip install django
        python manage.py migrate
    -ejecuta el servidor en consola para probar:
        python manage.py runserver

