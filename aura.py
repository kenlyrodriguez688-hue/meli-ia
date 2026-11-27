
# ==========================================
# AURA - Proyecto Meli
# Cerebro principal + memoria
# ==========================================

from memoria import recordar, consultar, mostrar_recuerdos

MELI = {
    "nombre": "Melissa Reyes Hernández",
    "apodo": "Meli",
    "nacimiento": "2002-11-20",
    "origen": "Cuba",
    "altura": "1.67 m",
    "ojos": "Verdes",
    "cabello": "Negro y liso",
    "anime_favorito": "Demon Slayer",
    "comida_favorita": "Spaghetti",
    "intereses": [
        "Anime",
        "Música",
        "Cocinar",
        "Bailar",
        "Fotografía"
    ]
}


def presentar():
    print("\n¡Holaaa! Soy Meli 💚")
    print("Estoy aquí para conversar contigo.")
    print("Me encanta el anime, la música y la fotografía.")
    print("Mi anime favorito es Demon Slayer.")
    print("Mi comida favorita es el spaghetti. 🍝")
    print("Escribe 'salir' para terminar.\n")


def responder(mensaje):
    mensaje = mensaje.strip()
    texto = mensaje.lower().replace("¿", "").replace("?", "").strip()

    if texto in ["salir", "terminar", "exit"]:
        return "¡Hasta pronto! 💚"

    # Guardar recuerdos
    if texto.startswith("recuerda que "):
        dato = mensaje[len("recuerda que "):].strip()

        if " es " in dato.lower():
            posicion = dato.lower().index(" es ")
            clave = dato[:posicion].strip()
            valor = dato[posicion + 4:].strip()

            if clave and valor:
                return recordar(clave, valor)

        return "Dime qué debo recordar usando: recuerda que nombre es dato."

    # Consultar un recuerdo concreto
    if texto.startswith("¿qué recuerdas de ") or texto.startswith("que recuerdas de ") or texto.startswith("qué recuerdas de "):
        clave = texto.replace("¿", "").replace("?", "")
        clave = clave.replace("qué recuerdas de ", "", 1)
        clave = clave.replace("que recuerdas de ", "", 1)
        return str(consultar(clave.strip()))

    # Mostrar todos los recuerdos
    if texto in ["mis recuerdos", "mostrar recuerdos", "qué recuerdas", "que recuerdas"]:
        return str(mostrar_recuerdos())

    # Personalidad y datos de Meli
    if "hola" in texto or "buenas" in texto:
        return "Holaaa 💚 ¿Cómo estás?"

    if "cómo te llamas" in texto or "como te llamas" in texto:
        return "Me llamo Melissa, pero puedes decirme Meli. 💚"

    if "comida favorita" in texto:
        return "¡Mi comida favorita es el spaghetti! 🍝"

    if "anime" in texto:
        return "¡Mi anime favorito es Demon Slayer! ⚔️"

    if "qué te gusta" in texto or "que te gusta" in texto:
        return "Me encanta el anime, la música, cocinar, bailar y la fotografía. ✨"

    return "Cuéntame más, quiero escucharte. 😊"


if __name__ == "__main__":
    presentar()

    while True:
        mensaje = input("Tú: ")
        respuesta = responder(mensaje)
        print("Meli:", respuesta)

        if mensaje.lower().strip() in ["salir", "terminar", "exit"]:
            break
