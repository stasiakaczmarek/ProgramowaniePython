from flask import Flask, render_template, request, redirect, url_for, flash
from collections import defaultdict
from datetime import datetime

app = Flask(__name__)
# Musimy dodać secret key wymagany do używania flash messages
app.secret_key = "tajny_klucz"

# Lista zadań przechowywana w zmiennej w Pythonie
tasks = [
    {"id": 1, "content": "Posprzątać mieszkanie", "done": False, "due_date": "06-04-2025"},
    {"id": 2, "content": "Zrobić projekt na studia", "done": False, "due_date": "06-04-2025"},
    {"id": 3, "content": "Umyć samochód", "done": False, "due_date": "06-04-2025"}
]

# Wyświetlamy stronę główną
@app.route("/")
def home():
    return render_template("home.html")

# Wyświetlamy stronę z zadaniami
@app.route("/tasks", methods=["GET", "POST"])
def tasks_page():
    if request.method == "POST":
        # Pobramy nowp dodane zadanie z formularza
        new_task_content = request.form["content"]
        # Walidujemy i formatujemy datę
        due_date = validate_and_format_date(request.form["due_date"])
        if not due_date:
            flash("Nieprawidłowy format daty!")
            return redirect(url_for("tasks_page"))

        # Dodajemy nowe zadanie
        if new_task_content.strip():
            # Generujemy nowe id
            new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
            # Dodajemy nowe zadanie do listy
            tasks.append({
                "id": new_id,
                "content": new_task_content,
                "done": False,
                "due_date": due_date
            })
            return redirect(url_for("tasks_page"))

    # Grupujemy zadania według daty
    tasks_by_date = defaultdict(list)
    today = datetime.now().strftime("%d-%m-%Y")

    for task in tasks:
        # Sprawdzamy, czy zadanie nie jest już po terminie wykonania
        task["is_overdue"] = datetime.strptime(task["due_date"], "%d-%m-%Y") < datetime.strptime(today, "%d-%m-%Y")
        tasks_by_date[task["due_date"]].append(task)

    # Sortujemy daty
    sorted_dates = sorted(tasks_by_date.keys(),
                         key=lambda x: datetime.strptime(x, "%d-%m-%Y"),
                         reverse=True)

    # Renderujemy szablonn z danymi
    return render_template("tasks.html",
                         dates=sorted_dates,
                         tasks_by_date=tasks_by_date,
                         today=today)

# Funkcja do walidacji i formatowania daty
def validate_and_format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return None

# Usuwamy zadania
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    # Usuwamy zadania o podanym ID
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("tasks_page"))

# Oznaczamy zadanie jako wykonane
@app.route("/done/<int:task_id>")
def mark_as_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            # Zmieniamy status zadania na przeciwny jakbyśmy się rozmyślili
            task["done"] = not task["done"]
            break
    return redirect(url_for("tasks_page"))

# Wyświetlamy stronę "O aplikacji"
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)