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

class Smartphone:
    def __init__(self, model, producent):
        self.telefon = Telefon(model, producent)
        self.komunikacja = Komunikacja()
        self.rozrywka = Rozrywka()

    def __str__(self):
        return str(self.telefon)

    def wyslij_wiadomosc(self, odbiorca, tresc):
        self.komunikacja.wyslij_wiadomosc(odbiorca, tresc)

    def odtworz_muzyke(self, utwor):
        self.rozrywka.odtworz_muzyke(utwor)

# Test
smartphone = Smartphone("iPhone XS Max", "Apple")
print("Jaki masz telefon?\n", smartphone)
print("Czy możesz wysyłać wiadomości?")
smartphone.wyslij_wiadomosc("Anastazja Kaczmarek", "Hejka! Co robisz?")
print("Czy możesz odtworzyć muzykę?")
smartphone.odtworz_muzyke("Bohemian Rhapsody")

# Zalety
# Każda klasa odpowiada za jedną funkcjonalność
# Nie ma ryzyka konfliktu metod, które mogłyby wystąpić w przypadku wielodziedziczenia