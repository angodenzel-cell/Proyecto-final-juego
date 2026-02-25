 Proyecto-final-juego
 
  mi juego de piedra, papel y tijeras

Bienvenido al repositorio de mi juego . Este proyecto es una aplicación de consola en Python que utiliza una arquitectura de módulos separando la lógica en una biblioteca externa.

1. Estructura del Proyecto

1.1_ **`juego_de_bruce_2.py`**: Código principal que contiene el bucle de ejecución y la interacción con el usuario.

1.2_ **`biblioteca_bruce_3.py`**: Módulo que contiene las funciones lógicas como `inicializar_juego`, `obtener_resultado` y `mostrar_marcador`

2_ Diagrama de Flujo (Lógica del código)

A continuación se muestra cómo funciona el bucle de repetición `while True` y cómo interactúa con la biblioteca, es un apartado donde se puede ver la extructura del codigo resumida a contimuacion dejo el enlace;

![Diagrama de Flujo del Juego](https://r.jina.ai/i/6f9012a9c735467498c39e25d2d5a3ec) 

3:Comandos y Funciones Utilizadas

En el Bucle Principal (`while True`):

1: **`inicializar_juego()`**: Configura los puntos y las opciones iniciales.
2_**`mostrar_marcador()`**: Imprime el estado actual del juego.
3_**`input().lower().strip()`**: Captura y limpia la elección del usuario.
4_**`random.choice()`**: La computadora elige una opción al azar.
5_**`obtener_resultado()`**: Determina si hay empate o quién gana la ronda.

4_Opciones de Salida y Validación:

1_**`if usuario == "salir"`**: Rompe el bucle (`break`) y finaliza el programa.
2_**`if usuario not in opciones`**: Valida que la entrada sea correcta; si no, reinicia el bucle (`continue`)

5_Especificaciones Visuales

El flujo de trabajo ha sido diseñado con una paleta de colores **Azul y Blanco** para diferenciar claramente los procesos de biblioteca de las decisiones lógicas del sistema.
