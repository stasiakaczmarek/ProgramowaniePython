# Definiujemy wyjątki
# Jeśli brak użytkownika w systemie
class UserNotFoundError(Exception):
    pass

# Jeśli hasło jest niepoprawne
class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        # Tworzymy słownik przechowujący loginy i hasła ({login: hasło})
        self.users = users

    def login(self, username, password):
        # Sprawdzamy czy taki użytkownik jest w systemie
        if username not in self.users:
            raise UserNotFoundError(f"Brak użytkownik o nazwie '{username}' w systemie.")

        # Sprawdzamy, czy hasło jest poprawne
        if self.users[username] != password:
            raise WrongPasswordError(f"Nieprawidłowe hasło dla użytkownika '{username}'.")

        # Jeśli wszystko jest OK
        return f"Użytkownik '{username}' zalogowany pomyślnie."


# Test
auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    print(auth.login("admin", "1234"))
    # Jeśli wszystko jest OK
except Exception as e:
    print(f"Błąd: {e}")

try:
    print(auth.login("admin1234", "1234"))
    # Jeśli brak użytkownika w systemie
except Exception as e:
    print(f"Błąd: {e}")

try:
    print(auth.login("user", "1234"))
    # Jeśli hasło jest niepoprawne
except Exception as e:
    print(f"Błąd: {e}")