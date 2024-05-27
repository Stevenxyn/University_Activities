# Solicitud con la cual se le pidio a ChatGPT el chatbot

Quiero un programa en que funcione con python, sera un Chatbot en cual me debe recomendar canciones de Cigarettes after sex y metallica

Dame el codigo para copiar y pegar.

## Respuesta del codigo suministrada



```python
import random

class MusicChatbot:
    def __init__(self):
        self.cigarettes_after_sex_songs = [
            "Nothing's Gonna Hurt You Baby",
            "Apocalypse",
            "Sweet",
            "K.",
            "Each Time You Fall In Love",
            "Sunsetz",
            "Heavenly"
        ]
        self.metallica_songs = [
            "Enter Sandman",
            "Nothing Else Matters",
            "Master of Puppets",
            "One",
            "The Unforgiven",
            "Sad But True",
            "Fade to Black"
        ]

    def recommend_song(self, band_name):
        if band_name.lower() == "cigarettes after sex":
            return random.choice(self.cigarettes_after_sex_songs)
        elif band_name.lower() == "metallica":
            return random.choice(self.metallica_songs)
        else:
            return "Lo siento, no tengo recomendaciones para esa banda."

def main():
    chatbot = MusicChatbot()
    print("¡Hola! Soy tu chatbot de recomendaciones musicales.")
    while True:
        band = input("¿De qué banda te gustaría una recomendación (Cigarettes After Sex o Metallica)? o escribe 'salir' para terminar: ")
        if band.lower() == 'salir':
            break
        recommendation = chatbot.recommend_song(band)
        print(f"Te recomiendo escuchar: {recommendation}")

if __name__ == "__main__":
    main()

```

## Respuesta total suministrada 

or supuesto, aquí tienes un sencillo programa en Python para un chatbot que recomienda canciones de las bandas "Cigarettes After Sex" y "Metallica". Utilizaremos una lista fija de canciones para cada banda y seleccionaremos una canción al azar para la recomendación.

python
Copy code
import random

class MusicChatbot:
    def __init__(self):
        self.cigarettes_after_sex_songs = [
            "Nothing's Gonna Hurt You Baby",
            "Apocalypse",
            "Sweet",
            "K.",
            "Each Time You Fall In Love",
            "Sunsetz",
            "Heavenly"
        ]
        self.metallica_songs = [
            "Enter Sandman",
            "Nothing Else Matters",
            "Master of Puppets",
            "One",
            "The Unforgiven",
            "Sad But True",
            "Fade to Black"
        ]

    def recommend_song(self, band_name):
        if band_name.lower() == "cigarettes after sex":
            return random.choice(self.cigarettes_after_sex_songs)
        elif band_name.lower() == "metallica":
            return random.choice(self.metallica_songs)
        else:
            return "Lo siento, no tengo recomendaciones para esa banda."

def main():
    chatbot = MusicChatbot()
    print("¡Hola! Soy tu chatbot de recomendaciones musicales.")
    while True:
        band = input("¿De qué banda te gustaría una recomendación (Cigarettes After Sex o Metallica)? o escribe 'salir' para terminar: ")
        if band.lower() == 'salir':
            break
        recommendation = chatbot.recommend_song(band)
        print(f"Te recomiendo escuchar: {recommendation}")

if __name__ == "__main__":
    main()
Cómo usar el programa
Copia el código y pégalo en un archivo Python, por ejemplo, music_chatbot.py.
Ejecuta el archivo desde tu terminal o entorno de desarrollo integrado (IDE) con python music_chatbot.py.
Interactúa con el chatbot escribiendo el nombre de la banda ("Cigarettes After Sex" o "Metallica")

Para obtener una recomendación de canción.
Escribe "salir" para terminar la interacción.
¡Espero que disfrutes de tu chatbot de recomendaciones musicales!

# Ejemplos de uso



[[Abir Imagen](https://prnt.sc/STMBS9QYhFrE)]


