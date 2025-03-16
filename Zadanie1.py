import json

class ModelAI:
    # Atrybut klasowy przechowujący liczbę utworzonych modeli
    licznik_modeli = 0

    def __init__(self, nazwa_modelu, wersja):
        self.nazwa_modelu = nazwa_modelu
        self.wersja = wersja
        # Zwiększamy licznik modeli przy każdym utworzeniu nowego obiektu
        self.nowy_model()

    @classmethod
    def nowy_model(cls):
        # Zwiększa licznik utworzonych modeli
        cls.licznik_modeli = cls.licznik_modeli + 1

    @classmethod
    def liczba_modeli(cls):
        # Zwraca liczbę utworzonych modeli
        return cls.licznik_modeli

    @classmethod
    def utworz_z_pliku(cls, nazwa_pliku):
        # Tworzy obiekt na podstawie pliku .json
        with open(nazwa_pliku, 'r') as plik:
            dane = json.load(plik)
            nazwa_modelu = dane.get('name')
            wersja = dane.get('version')
            return cls(nazwa_modelu, wersja)

# Tworzymy model na podstawie pliku JSON
model = ModelAI.utworz_z_pliku('model.json.txt')

print(f"Nazwa modelu: {model.nazwa_modelu}\n"
      f"Wersja modelu: {model.wersja}\n"
      f"Liczba utworzonych modeli: {ModelAI.liczba_modeli()}")

