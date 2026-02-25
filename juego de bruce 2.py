# -*- coding: utf-8 -*-
"""
Archivo: biblioteca_bruce.py
Proyecto: Juego de Piedra, Papel o Tijera ( Biblioteca)
"""
import random

from biblioteca_bruce import inicializar_juego,obtener_resultado,mostrar_marcador


# ZONA DE EJECUCIÓN (El codigo principal)


def jugar():
    """Función principal que controla el bucle y usa la biblioteca."""
    # 1. Preparación llamando a la biblioteca
    puntos_usuario, puntos_computadora, opciones = inicializar_juego()
    
    print("--- BIENVENIDO AL JUEGO DE BRUCE ---")
    
    # 2. Bucle principal
    while True: 
        mostrar_marcador(puntos_usuario, puntos_computadora)
        usuario = input("Elige piedra, papel, tijera (o 'salir'): ").lower().strip()
        
        # 3. Salida
        if usuario == "salir": 
            print("Finalizando programa...")
            break
            
        # 4. Validación
        if usuario not in opciones: 
            print("¡Error! Opción no válida. Intenta de nuevo.")
            continue

        # 5. Turno de la PC
        computadora = random.choice(opciones)
        print(f"Computadora eligió: {computadora}")

        # 6. Uso de la biblioteca para decidir el ganador
        resultado = obtener_resultado(usuario, computadora)
        
        if resultado == "empate":
            print("=> Es un EMPATE.")
        elif resultado == "usuario":
            print("=> ¡GANASTE ESTA RONDA!")
            puntos_usuario += 1
        else:
            print("=> PERDISTE ESTA RONDA.")
            puntos_computadora += 1

    # 7. Marcador Final
    print("-" * 27)
    print(f"Resultado Final: Usuario {puntos_usuario} | Computadora {puntos_computadora}")
    print("Desarrollo finalizado.")

# Punto de entrada del programa
if __name__ == "__main__":
    jugar()