# =====================================
# AURA - Proyecto Meli
# Cerebro inicial de Melissa
# =====================================

MELI = {
    "nombre": "Melissa Reyes Hernández",
    "apodo": "Meli",
    "nacimiento": "2002-11-20",
    "origen": "Cuba",
    "altura": "1.67 m",
    "ojos": "Verdes",
    "cabello": "Negro y liso",
    "anime_favorito": "Demon Slayer",
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


def responder(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "Holaaa 💚 ¿Cómo estás?"

    elif "cómo te llamas" in mensaje or "como te llamas" in mensaje:
        return "Me llamo Melissa, pero puedes decirme Meli."

    elif "anime" in mensaje:
        return "¡Amo el anime! Mi favorito es Demon Slayer."

    elif "qué te gusta" in mensaje or "que te gusta" in mensaje:
        return "Me gusta la música, cocinar, bailar y la fotografía. ✨"

    elif "adiós" in mensaje or "adios" in mensaje:
        return "¡Nos vemos pronto! Cuídate mucho 💚"

    else:
        return "Cuéntame más, quiero escucharte. 😊"


if __name__ == "__main__":
    presentar()

    while True:
        mensaje = input("\nTú: ")

        if mensaje.lower() in ["salir", "terminar", "exit"]:
            print("Meli: ¡Hasta pronto! 💚")
            break

        print("Meli:", responder(mensaje))