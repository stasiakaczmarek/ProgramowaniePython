from flask import Flask, render_template

app = Flask(__name__)

# Przykładowe dane użytkowników
users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}

# Wyświetlamy stronę główną z powitaniem i linkami do innych podstron
@app.route("/")
def home():
    return '''
        <h1>Cześć!</h1>
        <nav>
            <ul>
                <li><a href="/about">O nas</a></li>
                <li><a href="/users">Lista użytkowników</a></li>
            </ul>
        </nav>
    '''

# Wyświetlamy „O nas”
@app.route("/about")
def about():
    return '''
        <h1>O nas</h1>
        <p>Jesteśmy nowym portalem, na którym musisz mieć swój własny profil!</p>
        <a href="/">Powrót do strony głównej</a>
    '''

# Lista użytkowników (dane zapisane w słowniku)
@app.route("/users")
def users_list():
    users_links = []
    for user_id, user_info in users.items():
        users_links.append(f'<li><a href="/user/{user_id}">{user_info["name"]}</a></li>')

    return f'''
        <h1>Lista użytkowników</h1>
        <ul>{"".join(users_links)}</ul>
        <a href="/">Powrót do strony głównej</a>
    '''

# Profil konkretnego użytkownika (dynamiczny routing)
@app.route("/user/<int:user_id>")
def user_profile(user_id):
    user = users.get(user_id)
    if user:
        return f'''
            <h1>Profil użytkownika</h1>
            <p>{user["name"]}, {user["age"]} lat</p>
            <a href="/users">Powrót do listy użytkowników</a>
        '''
    else:
        return '''
            <h1>Użytkownik nie istnieje</h1>
            <a href="/users">Powrót do listy użytkowników</a>
        ''', 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)