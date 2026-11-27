
# ==========================================
# AURA - Proyecto Meli
# Cerebro + memoria
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
    mensaje = mensaje.strip()
    texto = mensaje.lower()

    if texto in ["salir", "terminar", "exit"]:
        return "¡Hasta pronto! 💚"

    if texto.startswith("recuerda que "):
        dato = mensaje[len("recuerda que "):].strip()

        if " es " in dato.lower():
            posicion = dato.lower().index(" es ")
            clave = dato[:posicion].strip()
            valor = dato[posicion + 4:].strip()

            if clave and valor:
                return recordar(clave, valor)

        return "Dime qué debo recordar usando: recuerda que nombre es dato."

    if texto.startswith("recuerda "):
        dato = mensaje[len("recuerda "):].strip()

        if " es " in dato.lower():
            posicion = dato.lower().index(" es ")
            clave = dato[:posicion].strip()
            valor = dato[posicion + 4:].strip()

            if clave and valor:
                return recordar(clave, valor)

        return "Prueba así: recuerda que tu comida favorita es pizza."

    if texto.startswith("qué recuerdas de ") or texto.startswith("que recuerdas de "):
        clave = mensaje.split(" ", 3)[-1].strip(" ?¿")
        return str(consultar(clave))

    if texto in ["mis recuerdos", "mostrar recuerdos", "qué recuerdas", "que recuerdas"]:
        return str(mostrar_recuerdos())

    if "hola" in texto:
        return "Holaaa 💚 ¿Cómo estás?"

    if "cómo te llamas" in texto or "como te llamas" in texto:
        return "Me llamo Melissa, pero puedes decirme Meli."

    if "anime" in texto:
        return "¡Amo el anime! Mi favorito es Demon Slayer."

    if "qué te gusta" in texto or "que te gusta" in texto:
        return "Me gusta la música, cocinar, bailar y la fotografía. ✨"

    return "Cuéntame más, quiero escucharte. 😊"


if __name__ == "__main__":
    presentar()
    print("\nPuedes escribirme normalmente.")
    print("Para guardar: recuerda que comida favorita es pizza.")
    print("Para consultar: ¿qué recuerdas de comida favorita?")
    print("Escribe salir para terminar.\n")

    while True:
        mensaje = input("Tú: ")
        respuesta = responder(mensaje)
        print("Meli:", respuesta)

        if mensaje.strip().lower() in ["salir", "terminar", "exit"]:
            break
