# =====================================
# AURA - Memoria de Meli
# =====================================

import json
import os

ARCHIVO_MEMORIA = "memoria_meli.json"


def cargar_memoria():
    if os.path.exists(ARCHIVO_MEMORIA):
        try:
            with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (json.JSONDecodeError, OSError):
            return {}

    return {}


def guardar_memoria(memoria):
    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as archivo:
        json.dump(memoria, archivo, ensure_ascii=False, indent=4)


def recordar(clave, dato):
    memoria = cargar_memoria()
    memoria[clave.lower()] = dato
    guardar_memoria(memoria)
    return f"¡Lo recordaré! 💚 Guardé: {clave}"


def consultar(clave):
    memoria = cargar_memoria()
    return memoria.get(clave.lower(), "Todavía no tengo ese recuerdo.")


def mostrar_recuerdos():
    memoria = cargar_memoria()

    if not memoria:
        return "Todavía no tengo recuerdos guardados."

    return memoria


if __name__ == "__main__":
    print("💚 Memoria de Meli preparada.")
    print("Escribe 'salir' para terminar.")

    while True:
        accion = input("\n¿Qué quieres hacer? (guardar / consultar / salir): ").lower()

        if accion == "guardar":
            clave = input("¿Qué debo recordar?: ")
            dato = input("¿Cuál es el dato?: ")
            print(recordar(clave, dato))

        elif accion == "consultar":
            clave = input("¿Qué recuerdo buscas?: ")
            print(consultar(clave))

        elif accion == "salir":
            print("Hasta pronto 💚")
            break

        else:
            print("No entendí esa opción.")