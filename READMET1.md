# validacion-agreg-don.js - Información sobre las funciones de validación

Este archivo contiene funciones de validación utilizadas para asegurar la correcta entrada de datos en los formularios.

## Funciones de Validación

### 1. `validarNombre()`

- **Descripción:** Valida el nombre ingresado en el formulario.
- **Fuente de la Expresión Regular:** La expresión regular utilizada para validar nombres fue obtenida de [Stack Overflow en Español](https://es.stackoverflow.com/questions/498065/crear-una-expresion-regular-para-validar-nombres).

### 2. `validarEmail()`

- **Descripción:** Valida el correo electrónico ingresado en el formulario.
- **Fuente de la Función Base:** La validación del email se basa en la función descrita en [CoderBox](https://www.coderbox.net/blog/validar-email-usando-javascript-y-expresiones-regulares/).

### 3. `validarNumero()`

- **Descripción:** Valida el número de teléfono ingresado en el formulario.
- **Fuente de la Expresión Regular:** Esta función solo acepta números de teléfono chilenos. La expresión regular fue obtenida de [Gist](https://gist.github.com/jaimeguaman/5819511#file-regex_celulares_chile).

## Funciones de Manejo de Errores

### 1. `mostrarError(input, idName, mensaje)`

- **Descripción:** Crea y muestra un mensaje de error asociado a un campo de entrada (input) específico.
- **Parámetros:**
  - `input`: El elemento de entrada (input) donde ocurrió el error.
  - `idName`: Un identificador único para el mensaje de error.
  - `mensaje`: El texto del mensaje de error a mostrar.
- **Funcionamiento:**
  - La función verifica si ya existe un mensaje de error para el input dado. Si no existe, crea un nuevo elemento `div` para el mensaje de error y lo inserta después del input. El mensaje de error se muestra en color rojo y el borde del input se colorea también en rojo.

### 2. `limpiarError(input, idName)`

- **Descripción:** Limpia el mensaje de error asociado a un campo de entrada (input) específico.
- **Parámetros:**
  - `input`: El elemento de entrada (input) del cual se quiere limpiar el error.
  - `idName`: El identificador único para el mensaje de error que se desea limpiar.
- **Funcionamiento:**
  - La función busca el mensaje de error correspondiente al input y lo borra si existe. También restaura el color original del borde del input.

# ver-dispositivos.css - Información sobre la plantilla utilizada

El archivo `ver-dispositivos.css` se creó utilizando como plantilla un CSS obtenido del siguiente enlace, disponible en la documentación de MDN:

- **Fuente de la Plantilla:** [Minimal Table CSS - MDN Learning Area](https://github.com/mdn/learning-area/blob/main/html/tables/basic/minimal-table.css)

# info-del-dispositivo.js - Información sobre las imágenes

El tamaño de las imágenes difiere del solicitado con el propósito de evitar distorsiones y ajustarse al diseño de la página.
