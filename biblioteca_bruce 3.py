# ( funciones lógicas


def inicializar_juego():
    """Configura y devuelve las variables iniciales."""
    return 0, 0, ["piedra", "papel", "tijera"]

def obtener_resultado(usuario, computadora):
    """
    Compara las jugadas y determina el ganador.
    Devuelve: 'empate', 'usuario' o 'computadora'
    """
    if usuario == computadora:
        return "empate"
    
    # Lista de condiciones en las que el usuario gana
    victorias_usuario = [
        (usuario == "piedra" and computadora == "tijera"),
        (usuario == "papel" and computadora == "piedra"),
        (usuario == "tijera" and computadora == "papel")
    ]
    
    # Si alguna de las condiciones de victoria es verdadera (True)
    if any(victorias_usuario):
        return "usuario"
    else:
        return "computadora"

def mostrar_marcador(puntos_u, puntos_c):
    """Imprime el estado actual de los puntos."""
    print(f"\nMarcador Actual: Usuario {puntos_u} - Computadora {puntos_c}")

