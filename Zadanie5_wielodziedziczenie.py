class Telefon:
    def __init__(self, model, producent):
        self.model = model
        self.producent = producent

    def __str__(self):
        return f"Telefon: {self.producent} {self.model}"

class Komunikacja:
    def wyslij_wiadomosc(self, odbiorca, tresc):
        print(f"Wysłano wiadomość do {odbiorca}: {tresc}")

class Rozrywka:
    def odtworz_muzyke(self, utwor):
        print(f"Odtwarzanie utworu: {utwor}")

class Smartphone(Telefon, Komunikacja, Rozrywka):
    def __init__(self, model, producent):
        super().__init__(model, producent)

# Test
smartphone = Smartphone("iPhone XS Max", "Apple")
print("Jaki masz telefon?\n", smartphone)
print("Czy możesz wysyłać wiadomości?")
smartphone.wyslij_wiadomosc("Anastazja Kaczmarek", "Hejka! Co robisz?")
print("Czy możesz odtworzyc muzykę?")
smartphone.odtworz_muzyke("Bohemian Rhapsody")

# Zalety
# Klasy bazowe są niezależne
# Klasy nie mają wspólnych metod
# Jeśli klasy Komunikacja i Rozrywka miałyby metody o tej samej nazwie, mogłoby to prowadzić do konfliktów
