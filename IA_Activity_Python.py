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
    print("Hola profesor Libardo Gomez ;)")
    while True:
        band = input("¿De qué banda te gustaría una recomendación (Cigarettes After Sex o Metallica)? o escribe 'salir' para terminar: ")
        if band.lower() == 'salir':
            break
        recommendation = chatbot.recommend_song(band)
        print(f"Te recomiendo escuchar: {recommendation}")

if __name__ == "__main__":
    main()
