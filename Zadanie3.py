class TextAnalyzer:
    def word_count(self, text):
        # Zwracamy liczbę słów w tekście
        words = text.split()
        # print(words)
        return len(words)

    def char_count(self, text):
        # Zwracamy liczbę znaków w tekście
        return len(text)

    def unique_word_count(self, text):
        # Zwracamy liczbę unikalnych słów w tekście
        words = text.split()
        # print(words)
        unique_words = set(words)
        # print(unique_words)
        return len(unique_words)


class AdvancedTextAnalyzer(TextAnalyzer):
    def sentiment_analysis(self, text):
        positive_words = {"wspaniały", "pozytywny", "miły", "przyjemny", "fajny", "dobry", "fantastyczny", "świetny",
                          "znakomity", "cudowny", "idealny", "doskonały", "fenomenalny", "niesamowity", "rewelacyjny",
                          "genialny", "wymarzony", "radosny", "słoneczny", "pogodny", "beztroski", "udany", "szczęśliwy",
                          "inspirujący", "motywujący", "relaksujący", "spokojny", "harmonijny", "satysfakcjonujący"}

        negative_words = {"okropny", "negatywny", "nieprzyjemny", "straszny", "zły", "koszmarny", "przykry", "smutny",
                          "przygnębiający", "beznadziejny", "męczący", "uciążliwy", "deprymujący", "ponury", "chaotyczny",
                          "nerwowy", "stresujący", "rozczarowujący", "nudny", "mdły", "nieudany", "przytłaczający",
                          "przeciętny", "niefortunny", "kłopotliwy", "nieznośny", "denerwujący", "irytujący"}

        # Zamieniamy wszystkie litery w tekście na małe litery
        # Tworzymy zbiór z listy słów
        words = set(text.lower().split())
        # print(words)

        positive_count = len(words.intersection(positive_words))
        # print(positive_count)
        negative_count = len(words.intersection(negative_words))
        # print(negative_count)

        if positive_count > negative_count:
            return "pozytywny"
        elif negative_count > positive_count:
            return "negatywny"
        else:
            return "neutralny"

# Test
analyzer = AdvancedTextAnalyzer()
text1 = "To był naprawdę wspaniały dzień!"
text2 = "To był naprawdę okropny dzień!"
text3 = "To był normalny dzień"

print(f"Tekst: '{text1}'")
print(f"Liczba słów: {analyzer.word_count(text1)}")
print(f"Liczba znaków: {analyzer.char_count(text1)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text1)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text1)}\n")

print(f"Tekst: '{text2}'")
print(f"Liczba słów: {analyzer.word_count(text2)}")
print(f"Liczba znaków: {analyzer.char_count(text2)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text2)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text2)}\n")

print(f"Tekst: '{text3}'")
print(f"Liczba słów: {analyzer.word_count(text3)}")
print(f"Liczba znaków: {analyzer.char_count(text3)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text3)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text3)}\n")

# Sprawdzamy jak radzi sobie z dłuższymi tekstami
text4 = "Dzisiejszy poranek był fantastyczny – obudziłem się wyspany a na śniadanie zjadłem jajecznicę. Po południu spotkałem się z przyjaciółmi na spacer. Niestety, wieczorem wszystko się zmieniło – droga do domu okazała się koszmarna z powodu chaotycznego ruchu ulicznego, a na dodatek miałem stresujący telefon od szefa."

print(f"Tekst: '{text4}'")
print(f"Liczba słów: {analyzer.word_count(text4)}")
print(f"Liczba znaków: {analyzer.char_count(text4)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text4)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text4)}\n")

text5 = "Dzisiejszy dzień był wspaniały i radosny – od rana towarzyszyła mi słoneczna pogoda, a śniadanie było pyszne i przyjemne. Po południu miałam fantastyczne spotkanie z przyjaciółmi, a nasza rozmowa była inspirująca i motywująca. Wieczorem udało mi się zrelaksować przy spokojnej muzyce, co sprawiło, że cały dzień zakończył się satysfakcjonująco. To był idealny i beztroski dzień, który napełnił mnie szczęściem i harmonią."

print(f"Tekst: '{text5}'")
print(f"Liczba słów: {analyzer.word_count(text5)}")
print(f"Liczba znaków: {analyzer.char_count(text5)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text5)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text5)}\n")

text6 = "Dzisiejszy dzień był okropny i przygnębiający – od rana towarzyszył mi chaotyczny harmonogram, a śniadanie było mdłe i nieprzyjemne. Po południu miałam stresujące spotkanie w pracy, które okazało się rozczarowujące i beznadziejne. Wieczorem droga do domu była uciążliwa z powodu kłopotliwego ruchu ulicznego, a na dodatek czułam się przytłoczona obowiązkami. To był koszmarny i nerwowy dzień, który pozostawił mnie zmęczoną i zdołowaną."

print(f"Tekst: '{text6}'")
print(f"Liczba słów: {analyzer.word_count(text6)}")
print(f"Liczba znaków: {analyzer.char_count(text6)}")
print(f"Liczba unikalnych słów: {analyzer.unique_word_count(text6)}")
print(f"Wynik analizy: {analyzer.sentiment_analysis(text6)}\n")